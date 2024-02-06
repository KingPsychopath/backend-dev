from main import *

run_cases = [
    (
        (["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"]),
        [("Proposal", "docx"), ("Contract", "txt")],
    ),
    (
        (["Presentation", "Summary"], ["pptx", "docx"]),
        [("Presentation", "pptx"), ("Summary", "docx")],
    ),
]

submit_cases = run_cases + [
    (([], []), []),
    ((["Test", "Example"], ["ppt", "docx"]), [("Test", "ppt"), ("Example", "docx")]),
    (
        (
            ["Python Cheatsheet", "Java Cheatsheet", "Malware", "Golang Cheatsheet"],
            ["pdf", "docx", "trash", "docx"],
        ),
        [
            ("Python Cheatsheet", "pdf"),
            ("Java Cheatsheet", "docx"),
            ("Golang Cheatsheet", "docx"),
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * doc_names: {input1[0]}")
    print(f" * doc_formats: {input1[1]}")
    print(f"Expecting: {expected_output}")
    try:
        result = list(pair_document_with_format(*input1))
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()