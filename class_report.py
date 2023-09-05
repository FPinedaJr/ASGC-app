def get_scores(num_of_students: int) -> dict:
    """
    Take the ASSIGNMENT, QUIZ, FINAL EXAM of students 

    Args:
        number of students [int]

    Return
        students record [dict]
    """
    print("-----PLEASE SEPERATE BY A COMMA-----")
    students = {}
    for i in range(num_of_students):
        students[f"student_{i+1}"] = {}

    for i in range(num_of_students):
        students[f"student_{i+1}"]["assignments"] = input(f"ASSIGNMENT score of student {i+1}: ").split(',')
        students[f"student_{i+1}"]["quizzes"] = input(f"      QUIZ score of student {i+1}: ").split(',')
        students[f"student_{i+1}"]["final_exam"] = int(input(f"FINAL EXAM score of student {i+1}: "))
        print("\n")
    
    return students




def convert_scores_to_int(students: dict) -> dict:
    """
    Convert the scores of the students to integer

    Args:
        students [dict] -> str

    Return
        students [dict] -> int
    """
    num_of_students = len(students)
    for j in range(num_of_students):
        for i in range(len(students[f"student_{j+1}"]["assignments"])):
            students[f"student_{j+1}"]["assignments"][i] = int(students[f"student_{j+1}"]["assignments"][i])

        for i in range(len(students[f"student_{j+1}"]["quizzes"])):
            students[f"student_{j+1}"]["quizzes"][i] = int(students[f"student_{j+1}"]["quizzes"][i])

    return students




def seperate_scores(students: dict, type: str) -> dict:
    """
    Seperate the scores of the students

    Args:
        students [dict] 

    Return
        scores [dict]
    """
    num_of_scores = len(students[f"student_1"][type])
    num_of_students = len(students)

    scores = {}
    for i in range(num_of_scores):
        scores[f"score_{i+1}"] = []

    for j in range(num_of_students):
        for i in range(len(students[f"student_{j+1}"][type])):
            scores[f"score_{i+1}"].append(students[f"student_{j+1}"][type][i])
    
    return scores




def compile_final_exam(students: dict) -> list:
    """
    Compile the final exam of the students 

    Args:
        students [dict] 

    Return
        final exam [list] 
    """
    final_exam = []

    for i in range(len(students)):
        final_exam.append(students[f"student_{i+1}"]["final_exam"])

    return final_exam




def display_average(scores: list): 
    """
    Display the average of the students 

    Args:
        scores [list] 
    """
    sum_of_list = 0 
    for i in range(len(scores)): 
        sum_of_list += scores[i]
    average_student = sum_of_list/len(scores)
    print("     class average: ", round(average_student, 2))




def display_min_max(scores: list):
    """
    Display the minimum and maximum score of the class 

    Args:
        scores [list]  
    """
    min = scores[0]
    max = scores[0]
    for i in range(len(scores)): 
        if scores[i] > max: 
            max = scores [i]
        elif scores [i] < min: 
            min = scores [i]

    print("     lowest score:  ", min)
    print("     highest score: ", max)




def main():
    students_num_input = int(input("Enter the number of students: "))
    students_rec = get_scores(students_num_input)
    students_rec = convert_scores_to_int(students_rec)
    assignments = seperate_scores(students_rec, "assignments")
    quizzes = seperate_scores(students_rec, "quizzes")
    final_exam = compile_final_exam(students_rec)

    for i in range(len(assignments)):
        print(f"\nASSIGNMENT #{i+1}")
        display_average(assignments[f"score_{i+1}"])
        display_min_max(assignments[f"score_{i+1}"])

    for i in range(len(quizzes)):
        print(f"\nQUIZ #{i+1}")
        display_average(quizzes[f"score_{i+1}"])
        display_min_max(quizzes[f"score_{i+1}"])

    print()
    print("FINAL EXAM")
    display_average(final_exam)
    display_min_max(final_exam)
    
    
         




if __name__ == "__main__":
    main()