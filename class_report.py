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

