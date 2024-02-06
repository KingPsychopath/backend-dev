def get_test_score(answer_sheet, student_answers):
    correct_count = 0
    for correct, input in zip(answer_sheet, student_answers):
        if correct == input:
            correct_count += 1

    percentage_correct = (correct_count / len(answer_sheet)) * 100
    return percentage_correct
