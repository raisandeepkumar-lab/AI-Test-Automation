from github import Github
import os

def push_to_github(filename):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(os.getenv("GITHUB_REPO"))

    with open(filename, "r") as file:
        content = file.read()

    repo.create_file(
        path=f"tests/{filename}",
        message=f"Add test case {filename}",
        content=content,
        branch="main"
    )

push_to_github("test_scrum-1.py")