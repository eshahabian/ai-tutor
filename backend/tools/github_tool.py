from langchain.tools import tool
import requests

@tool
def github_tool(repo_url: str) -> str:
    """
    Review a GitHub repository and provide feedback.
    Use this when the user shares a GitHub repository URL and wants feedback or code review.
    Input should be the full GitHub URL like 'https://github.com/username/repo'.
    """
    try:
        # از URL اطلاعات username و repo رو بگیر
        # مثال: https://github.com/username/repo
        parts = repo_url.replace("https://github.com/", "").split("/")
        owner = parts[0]
        repo = parts[1]

        # از GitHub API اطلاعات repo رو بگیر
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(api_url)
        data = response.json()

        # اطلاعات مهم رو جمع کن
        info = f"""
        Repository: {data.get('full_name', 'Unknown')}
        Description: {data.get('description', 'No description')}
        Language: {data.get('language', 'Unknown')}
        Stars: {data.get('stargazers_count', 0)}
        Forks: {data.get('forks_count', 0)}
        Open Issues: {data.get('open_issues_count', 0)}
        Created: {data.get('created_at', 'Unknown')}
        Last Updated: {data.get('updated_at', 'Unknown')}
        """

        return f"REVIEW_GITHUB:{info}"

    except Exception as e:
        return f"Error reading repository: {str(e)}"