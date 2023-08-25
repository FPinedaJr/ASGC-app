def compute_weighted_average(assignment_scores, quiz_scores, final_exam_score):
    assignment_weight = 30
    quiz_weight = 30
    final_exam_weight = 40

    # total assignment scores
    sum_of_your_assignment_score = 0
    sum_of_total_assignment_score = 0
    for score in assignment_scores:
        score = str(score)

        your_score, total_score = score.split("/")

        sum_of_your_assignment_score += int(your_score)
        sum_of_total_assignment_score += int(total_score)

    total_assignment_scores = sum_of_your_assignment_score / sum_of_total_assignment_score

    # total quiz scores
    sum_of_your_quiz_score = 0
    sum_of_total_quiz_score = 0
    for score in quiz_scores:
        score = str(score)

        your_score, total_score = score.split("/")

        sum_of_your_quiz_score += int(your_score)
        sum_of_total_quiz_score += int(total_score)

    total_quiz_scores = sum_of_your_quiz_score / sum_of_total_quiz_score

    assignment_grade = total_assignment_scores * assignment_weight
    quiz_grade = total_quiz_scores * quiz_weight
    final_exam_grade = final_exam_score * final_exam_weight

    overall_grade = assignment_grade + quiz_grade + final_exam_grade
    rounded_overall_grade = round(overall_grade, 2)
    return rounded_overall_grade