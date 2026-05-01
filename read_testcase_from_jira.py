import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

def extract_description(desc):
    """
    Handles both Jira v2 (string) and v3 (ADF JSON) description formats
    """
    if not desc:
        return "No description available"

    # Case 1: Plain string (Jira Server / v2)
    if isinstance(desc, str):
        return desc

    # Case 2: Atlassian Document Format (ADF - JSON)
    if isinstance(desc, dict):
        try:
            text_parts = []

            def extract_text(content):
                for item in content:
                    if item.get("type") == "text":
                        text_parts.append(item.get("text", ""))
                    elif "content" in item:
                        extract_text(item["content"])

            extract_text(desc.get("content", []))
            return " ".join(text_parts)

        except Exception:
            return "Description parsing failed"

    return "Unsupported description format"

def fetch_jira_issues():
    url = f"{os.getenv('JIRA_URL')}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json"
    }

    auth = HTTPBasicAuth(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_API_TOKEN")
    )

    payload = {
        "jql": "project = SCRUM ORDER BY created DESC",
        "maxResults": 5,
        "fields": ["summary", "description"]
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)

    if response.status_code != 200:
        print("❌ Error:", response.status_code, response.text)
        return []

    data = response.json()

    issues = []
    for issue in data.get("issues", []):
        issues.append({
            "key": issue.get("key"),
            "summary": issue["fields"].get("summary"),
            "description": extract_description(issue["fields"].get("description"))
        })

    return issues

def update_jira(issue_key, result):
    url = f"{os.getenv('JIRA_URL')}/rest/api/3/issue/{issue_key}/comment"

    auth = HTTPBasicAuth(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_API_TOKEN")
    )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "body": f"Automation Test Result: {result}"
    }

    requests.post(url, json=data, headers=headers, auth=auth)

print(fetch_jira_issues())