def sum_scores(scores: list) -> float:
    """
    Sums a list that contains scores with string elements e.g. ["8/10", "29/30", "30/40", "100/100"]

    Args:
        scores - list of scores [list]

    Return
        the sum of the scores [float]
    """
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
    """
    Computes the weighted average

    Args:
        assignment_scores - list of assignment scores [list]
        quiz_scores - list of quiz scores [list]
        final_exam_score - list of final_exam scores [list]

    Return
        the calculated wighted average [float]
    """
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

def assign_letter_grade(weighted_average: float) -> str: 
    if weighted_average >= 90:
        average = 'A'

    elif weighted_average >= 80: 
        average = 'B'

    elif weighted_average >= 70: 
        average = 'C'

    elif weighted_average >= 60:
        average = 'D'

    elif weighted_average >= 0:
        average = 'F'

    return average 