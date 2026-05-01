import requests

def generate_testcases(issue):
    prompt = f"""
    You are a QA automation expert.

    Generate pytest test cases for the following Jira ticket.

    Title: {issue['summary']}
    Description: {issue['description']}

    Requirements:
    - Use pytest
    - Include edge cases
    - Use parameterization where possible
    - Return ONLY Python code
    - Only provide python
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "codellama",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        print("❌ Ollama Error:", response.text)
        return ""

    if "```" in response.json()["response"]:
        return response.json()["response"].split("```")[1]
    return response.json()["response"]