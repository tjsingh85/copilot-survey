import requests
import pandas as pd
import re
import argparse

def get_pull_requests(org_name, label, token):
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }

    repos_url = f"https://api.github.com/orgs/{org_name}/repos"
    repos = requests.get(repos_url, headers=headers).json()

    prs_with_label = [pr for repo in repos for pr in get_prs_for_repo(org_name, repo['name'], headers) if label in get_labels(pr)]

    return prs_with_label

def get_prs_for_repo(org_name, repo_name, headers):
    prs_url = f"https://api.github.com/repos/{org_name}/{repo_name}/pulls"
    return requests.get(prs_url, headers=headers).json()

def get_labels(pr):
    return [label['name'] for label in pr['labels']]

def get_answers(data):
    questions_and_options = re.findall(r'\*\*\*(.*?)\*\*\*(.*?)(?=\*\*\*|$)', data, re.DOTALL)
    return {question.strip(): get_selected_option(options) for question, options in questions_and_options}

def get_selected_option(options):
    selected_option = re.search(r'- \[X\] (.*?)\n', options)
    return selected_option.group(1) if selected_option else "N/A"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', help='GitHub token', required=True)
    args = parser.parse_args()

    pull_requests = get_pull_requests('REPLACE_ME_WITH_ORG_NAME', 'REPLACE_ME_WITH_PR_LABEL', args.token)

    df = pd.DataFrame(columns=['PR URL', 'Org', 'Repo', 'Creator', 'Used Copilot', 'Time Saved', 'Used Frequency', 'Continue Use'])

    for pr in pull_requests:
        org = pr['base']['repo']['owner']['login']
        pr_url = pr['html_url']
        pr_repo = pr['head']['repo']['name']
        creator = pr['user']['login']
        data = pr['body']
        answers = get_answers(data)

        df = df._append({
            'PR URL': pr_url,
            'Org': org,
            'Repo': pr_repo,
            'Creator': creator,
            'Used Copilot': answers.get("Did you use Copilot in this PR?", "N/A"),
            'Time Saved': answers.get("How much time(in minutes) did you save by using Copilot?", "N/A"),
            'Used Frequency': answers.get("For this PR, Copilot allowed me to spend less time searching external resources?", "N/A"),
            'Continue Use': answers.get("I felt more productive using Copilot for this PR?", "N/A")
        }, ignore_index=True)

    df.to_excel('pull_requests.xlsx', index=False)