def get_scores(num_of_students: int) -> list:
    """
    Take the ASSIGNMENT, QUIZ, FINAL EXAM of students 

    Args:
        number of students [int]

    Return
        students record [dict]
    """
    print("-----PLEASE SEPERATE BY A COMMA-----")
    students = []
    for i in range(num_of_students):
        students.append({})

    for i in range(num_of_students):
        students[i]["assignments"] = input(f"ASSIGNMENT score of student {i+1}: ").split(',')
        students[i]["quizzes"] = input(f"      QUIZ score of student {i+1}: ").split(',')
        students[i]["final_exam"] = int(input(f"FINAL EXAM score of student {i+1}: "))
        print("\n")
    
    
    return students




def convert_scores_to_int(students: list) -> list:
    """
    Convert the scores of the students to integer

    Args:
        students [dict] -> str

    Return
        students [dict] -> int
    """
    num_of_students = len(students)
    for j in range(num_of_students):
        for i in range(len(students[j]["assignments"])):
            students[j]["assignments"][i] = int(students[j]["assignments"][i])

        for i in range(len(students[j]["quizzes"])):
            students[j]["quizzes"][i] = int(students[j]["quizzes"][i])

    return students




def seperate_scores(students: list, type: str) -> list:
    """
    Seperate the scores of the students

    Args:
        students [dict] 

    Return
        scores [dict]
    """
    num_of_scores = len(students[0][type])
    num_of_students = len(students)

    scores = {}
    for i in range(num_of_scores):
        scores[f"score_{i+1}"] = []

    for j in range(num_of_students):
        for i in range(len(students[j][type])):
            scores[f"score_{i+1}"].append(students[j][type][i])
    
    return scores




def compile_final_exam(students: list) -> list:
    """
    Compile the final exam of the students 

    Args:
        students [dict] 

    Return
        final exam [list] 
    """
    final_exam = []

    for i in range(len(students)):
        final_exam.append(students[i]["final_exam"])

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