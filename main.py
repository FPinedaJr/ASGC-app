def sum_scores(scores: list) -> float:
    sum_of_your_score = 0
    sum_of_total_score = 0
    for score in scores:
        score = str(score)

        your_score, total_score = score.split("/")

        sum_of_your_score += int(your_score)
        sum_of_total_score += int(total_score)

    total_score = sum_of_your_score / sum_of_total_score
    return total_score



def compute_weighted_average(assignment_scores: list, quiz_scores: list, final_exam_score: list) -> float:
    assignment_weight = 30
    quiz_weight = 30
    final_exam_weight = 40


    total_assignment_scores = sum_scores(assignment_scores)
    total_quiz_scores = sum_scores(quiz_scores)
    total_final_exam_scores = sum_scores(final_exam_score)

    assignment_grade = total_assignment_scores * assignment_weight
    quiz_grade = total_quiz_scores * quiz_weight
    final_exam_grade = total_final_exam_scores * final_exam_weight

    overall_grade = assignment_grade + quiz_grade + final_exam_grade
    rounded_overall_grade = round(overall_grade, 2)
    return rounded_overall_grade

