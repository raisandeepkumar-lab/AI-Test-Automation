from read_testcase_from_jira import fetch_jira_issues, update_jira
from generate_test_cases_using_GenAI import generate_testcases
from save_the_test_case import save_test_file
from push_to_github import push_to_github


def main():
    issues = fetch_jira_issues()

    for issue in issues:
        print(f"Processing {issue['key']}")

        test_code = generate_testcases(issue)
        filename = save_test_file(issue['key'], test_code)
        push_to_github(filename)

if __name__ == "__main__":
    main()