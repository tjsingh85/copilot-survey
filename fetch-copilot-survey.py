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

    prs_with_label = []
    for repo in repos:
        prs_url = f"https://api.github.com/repos/{org_name}/{repo['name']}/pulls"
        prs = requests.get(prs_url, headers=headers).json()
        for pr in prs:
            labels = [label['name'] for label in pr['labels']]
            if label in labels:
                prs_with_label.append(pr)

    return prs_with_label

# Create an empty DataFrame
df = pd.DataFrame(columns=['PR URL', 'Org', 'Repo', 'Creator', 'Used Copilot', 'Time Saved', 'Used Frequency', 'Continue Use'])

for pr in pull_requests:
    org = pr['base']['repo']['owner']['login']
    pr_url = pr['html_url']
    pr_repo = pr['head']['repo']['name']
    creator = pr['user']['login']
    data = pr['body']

    questions_and_options = re.findall(r'\*\*\*(.*?)\*\*\*(.*?)(?=\*\*\*|$)', data, re.DOTALL)
    answers = {}

    for question, options in questions_and_options:
        question = question.strip()
        selected_option = re.search(r'- \[X\] (.*?)\n', options)
        if selected_option:
            answers[question] = selected_option.group(1)
        else:
            answers[question] = "N/A"

    # Append the data to the DataFrame
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

# Export the DataFrame to an Excel file
df.to_excel('pull_requests.xlsx', index=False)

# Usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-token', type=str, help='GitHub token', required=True)
    args = parser.parse_args()

    pull_requests = get_pull_requests('org-name', 'label', args.token)