def get_scores():

    students = {
        "student_1": {},
        "student_2": {},
        "student_3": {},
        "student_4": {},
        "student_5": {},
    }

    for i in range(5):
        students[f"student_{i+1}"]["assignments"] = input(f"Enter the assignment of student {i+1}: ").split(',')
        students[f"student_{i+1}"]["quizzes"] = input(f"Enter the quizzes of student {i+1}: ").split(',')
        students[f"student_{i+1}"]["final_exam"] = int(input(f"Enter final exam of student {i+1}: "))
        print("\n")
    
    return students




def convert_scores_to_int(students):
    for j in range(5):
        for i in range(len(students[f"student_{j+1}"]["assignments"])):
            students[f"student_{j+1}"]["assignments"][i] = int(students[f"student_{j+1}"]["assignments"][i])

        for i in range(len(students[f"student_{j+1}"]["quizzes"])):
            students[f"student_{j+1}"]["quizzes"][i] = int(students[f"student_{j+1}"]["quizzes"][i])

    return students



def seperate_assignments(students):
    assignments = {
        "assignment_1": [],
        "assignment_2": [],
        "assignment_3": [],
        "assignment_4": [],
        "assignment_5": [],
        "assignment_6": [],
        "assignment_7": []
    }

    for j in range(5):
        for i in range(len(students[f"student_{j+1}"]["assignments"])):
            assignments[f"assignment_{i+1}"].append(students[f"student_{j+1}"]["assignments"][i])
    
    return assignments


def seperate_quizzes(students):
    quizzes = {
        "quizzes_1": [],
        "quizzes_2": [],
        "quizzes_3": [],
        "quizzes_4": [],
        "quizzes_5": [],
    }

    for j in range(5):
        for i in range(len(students[f"student_{j+1}"]["quizzes"])):
            quizzes[f"quizzes_{i+1}"].append(students[f"student_{j+1}"]["quizzes"][i])
    
    return quizzes



def compile_final_exam(students):
    final_exam = []

    for i in range(len(students)):
        final_exam.append(students[f"student_{i+1}"]["final_exam"])

    return final_exam


def display_average(arr): 
    sum_of_list = 0 
    for i in range(len(arr)): 
        sum_of_list += arr[i]
    average_student = sum_of_list/len(arr)
    print("     class average : ", round(average_student, 2))


def display_min_max(arr):
    min = arr [0]
    max = arr [0]
    for i in range(len(arr)): 
        if arr[i] > max: 
            max = arr [i]
        elif arr [i] < min: 
            min = arr [i]

    print("     lowest score: ", min)
    print("     highest score: ", max)


def main():
    students_rec = get_scores()
    students_rec = convert_scores_to_int(students_rec)
    assignments = seperate_assignments(students_rec)
    quizzes = seperate_quizzes(students_rec)
    final_exam = compile_final_exam(students_rec)

    for i in range(len(assignments)):
        print()
        print(f"ASSIGNMENT #{i+1}")
        display_average(assignments[f"assignment_{i+1}"])
        display_min_max(assignments[f"assignment_{i+1}"])

    for i in range(len(quizzes)):
        print()
        print(f"QUIZ #{i+1}")
        display_average(quizzes[f"quizzes_{i+1}"])
        display_min_max(quizzes[f"quizzes_{i+1}"])

    print()
    print("FINAL EXAM")
    display_average(final_exam)
    display_min_max(final_exam)

