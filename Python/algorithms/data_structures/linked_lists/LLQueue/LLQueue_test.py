from LLQueue import *

run_cases = [
    (
        ["Dagger", "Spear", "Staff", "Axe", "Bow", "Sword"],
        ["Spear", "Staff", "Axe", "Bow", "Sword"],
        "Dagger",
    ),
    (
        ["Spear", "Staff", "Axe", "Bow", "Sword"],
        ["Staff", "Axe", "Bow", "Sword"],
        "Spear",
    ),
    (["Staff", "Axe", "Bow", "Sword"], ["Axe", "Bow", "Sword"], "Staff"),
]

submit_cases = run_cases + [
    (["Axe"], [], "Axe"),
    (["Axe", "Bow", "Sword"], ["Bow", "Sword"], "Axe"),
    (["Bow", "Sword"], ["Sword"], "Bow"),
]


def test(linked_list, expected_state, expected_head):
    print("---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f" - Removing Head")
    print(f"Expected Head: {expected_head}")
    print(f"Expected List: {expected_state}")
    try:
        head = linked_list.remove_from_head()
        result = linked_list_to_list(linked_list)
    except Exception as e:
        result = f"Error: {e}"
        print("Fail")
        return False
    print(f"Actual Head: {head}")
    print(f"Actual List: {result}\n")
    if result == expected_state and head.val == expected_head:
        print("Pass")
        return True
    print("Fail")
    return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        linked_list = LLQueue()
        for item in test_case[0]:
            linked_list.add_to_tail(Node(item))
        correct = test(linked_list, test_case[1], test_case[2])
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