def get_test_score(answer_sheet, student_answers):
    name = student_answers[0]
    score = 0

    for answer, student_answer_index in zip(answer_sheet, range(1, len(student_answers))):
        if answer == student_answers[student_answer_index]:
            score += 1

    percentage = score / len(answer_sheet) * 100

    return name, percentage


def get_test_score2(answer_sheet, student_answers):
    score = 0
    student_name = student_answers[0]
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i + 1]:
            score += 1
    percentage = score / len(answer_sheet) * 100
    return student_name, percentage