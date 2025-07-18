from students.data import students

def get_subject_information():
    subjects = []
    no_of_subjects = input("Enter the number of subjects: ")

    while not no_of_subjects.isdigit() or int(no_of_subjects) <= 0:
        no_of_subjects = input("Invalid. Enter a valid number of subjects: ")
    no_of_subjects = int(no_of_subjects)

    for subject_index in range(no_of_subjects):
        subject = {
            "subject_name": "",
            "marks": 0
        }
        subject_name = input(f"Enter the name of subject {subject_index + 1}: ")
        while subject_name.isdigit():
            subject_name = input("Subject name cannot be a number. Enter again: ")

        marks = input(f"Enter marks in {subject_name}: ")
        while not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
            marks = input("Enter valid marks (0 to 100): ")

        subject["subject_name"] = subject_name
        subject["marks"] = int(marks)
        subjects.append(subject)

    return subjects


def get_student_information():
    no_of_students = input("Enter number of students: ")

    while not no_of_students.isdigit() or int(no_of_students) <= 0:
        no_of_students = input("Invalid. Enter a valid number of students: ")
    no_of_students = int(no_of_students)

    for student_index in range(no_of_students):
        student = {
            "student_name": "",
            "subjects": [],
            "average": 0
        }
        student_name = input(f"Enter the name of student {student_index + 1}: ")
        student["student_name"] = student_name
        print(f"Student name entered: {student_name}")
        subjects = get_subject_information()
        student["subjects"] = subjects

        total = sum(sub["marks"] for sub in subjects)
        student["average"] = round(total / len(subjects), 2)
        students.append(student)
