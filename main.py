import class_report
import student_grade


def main():
    module = int(input("[1] Compute a student's grade\n[2] Assess the class report\n"))
    print("\n=========================================")
    if module == 1:
        student_grade.main()
    elif module == 2:
        class_report.main()
    else:
        main()


if __name__ == "__main__":
    main()

