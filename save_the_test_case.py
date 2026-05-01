def save_test_file(issue_key, test_code):
    filename = f"test_{issue_key.lower()}.py"

    with open(filename, "w") as f:
        f.write(test_code)

    return filename