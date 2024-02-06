from main import *

run_cases = [
    (
        "John Thorton",
        ["Math", "English", "History"],
        [85, 92, 76],
        {"Math": "B", "English": "A", "History": "C"},
    ),
    (
        "Jasper Allen",
        ["Science", "Social Studies"],
        [90, 88],
        {"Science": "A", "Social Studies": "B"},
    ),
]

submit_cases = run_cases + [
    (
        "Bobby Christensen",
        ["Physics", "Chemistry", "Biology", "Geology"],
        [80, 78, 85, 90],
        {"Physics": "B", "Chemistry": "C", "Biology": "B", "Geology": "A"},
    ),
    (
        "Jack Sparrow",
        ["Treasure Hunting", "Sailing"],
        [70, 65],
        {"Treasure Hunting": "C", "Sailing": "D"},
    ),
    (
        "Tony Stark",
        ["Engineering", "Physics"],
        [100, 98],
        {"Engineering": "A", "Physics": "A"},
    ),
    (
        "Bruce Wayne",
        ["Martial Arts", "Detective Work"],
        [95, 92],
        {"Martial Arts": "A", "Detective Work": "A"},
    ),
    (
        "Peter Parker",
        ["Photography", "Biology"],
        [85, 88],
        {"Photography": "B", "Biology": "B"},
    ),
]


def test(student_name, courses, scores, expected_grades):
    print("---------------------------------")
    student = Student(student_name, scores)
    for i, course in enumerate(courses):
        student.add_course(course, scores[i])
    actual_grades = student.get_courses()

    print(f"Inputs for {student_name}:")
    print(f" * Courses: {courses}")
    print(f" * Scores: {scores}")
    print(f" * Expected Grades: {expected_grades}")
    print(f" * Actual Grades: {actual_grades}")

    if actual_grades == expected_grades:
        print("Pass")
        return True
    else:
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