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