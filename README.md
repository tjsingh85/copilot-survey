# copilot-survey

Conducting a GitHub Copilot survey during the pull request (PR) phase is benefical for several reasons:

- Real-time Feedback: Gathering feedback during the PR phase allows you to capture developers' experiences and impressions while they are actively using GitHub Copilot. This real-time feedback is often more accurate and reflective of their immediate experiences.

- Contextual Insights: Developers can provide context-specific insights during the PR phase. They can explain why they made certain choices, how GitHub Copilot helped them, and what challenges they encountered, providing richer and more relevant feedback.

- Accuracy of Time Savings: Assessing time savings during the PR phase provides a more accurate measurement of its impact. Developers can estimate time saved more precisely when they are actively engaged in the coding process.

- Identifying Adoption Challenges: Collecting feedback during PRs allows you to identify any adoption challenges developers face as they integrate GitHub Copilot into their workflow. This information is crucial for addressing hurdles and improving adoption rates.

- Better Engagement: Developers are more likely to participate in a survey when it aligns with their current tasks. Conducting the survey during the PR phase ensures higher engagement and participation rates.

- Iterative Improvement: With feedback collected during PRs, you can iteratively refine and enhance GitHub Copilot based on real-world usage patterns and pain points, leading to a more user-friendly and effective tool.

- In summary, conducting a GitHub Copilot survey during the PR phase allows you to gather timely, context-rich, and actionable feedback from developers, leading to a better understanding of the tool's impact and more effective improvements.

## Pre-Requiste
- Pull request template with copilot questions
- Set up github action for auto labelling the pull request with a unique label
- GitHub token to fetch data from GitHub Api

## How To Set Up Pull Request Template
When you add a pull request template to your repository, project contributors will automatically see the template's contents in the pull request body.If you havent created a pull request template before, you can check out the docs [here](https://docs.github.com/en/enterprise-cloud@latest/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

### How To Add Additional Questions
If you want to add more questions to pull request template, prefix and suffix your question with '***'. This is being use as question identifier in the regex pattern. See the pull_request_template.md in the root folder of this repo.

Also add the corresponding question in the fetch-copilot-survey.py in this section:
```
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
```

### How To Configure Answer Template
Simialr to questions, answers need to follow a certain writing standard because of the regex. Regex looks for selected option [X].

## Output Format
Once you run the python code, An excel file with survey results will be available in the root directory of the project.

## Auto Label Pull Request
- To auto label a pull request, you can use [labeler action](https://github.com/actions/labeler)
- To create a new label, follow the docs [here](https://docs.github.com/en/enterprise-cloud@latest/issues/using-labels-and-milestones-to-track-work/managing-labels)

## How to Run This Feature

### Codepsace
- open the codespaces
- provide org name , label and github token
```
  pull_requests = get_pull_requests('org-name', 'label', 'token')
```
- Run
```
python fetch-copilot-survey.py
```
- Excel file containing the results will be created in the root folder

### Locally
- git clone the repo
- hope you have python installed on your machine :). if not , you can download from [here](https://www.python.org/downloads/)
- install python dependencies using pip
```
pip install pandas
pip install openpyxl
pip install re
pip install requests
```
- provide org name , label and github token
```
  pull_requests = get_pull_requests('org-name', 'label', 'token')
```
- Run
```
python fetch-copilot-survey.py
```
- Excel file containing the results will be created in the root folder

## Feedback
If you have any feedback, feel free to open issues or pullrequest in this repo.

