# Get # of Students
# Loop through Students
# Get # of Subjects
# Subject Name and Mark in Subject

# Push to a list of dicts

# Enter options 
# Enter Student data
# 1 Display Marks by students and subject
# Top 3
# Average

students = []

def get_subject_information():
    subjects = []
    no_of_subjects = input("Enter the number of subjects: ")
    while not no_of_subjects.isdigit() or int(no_of_subjects) <= 0:
        no_of_subjects = input("Invalid. Enter a valid number of subjects: ")
    no_of_subjects = int(no_of_subjects)
    for subject_index in range(0, no_of_subjects):
        subject = {
            "subject_name":"",
            "marks": ""
        }
        subject_name = input(f"Enter the name of the subject {subject_index+1} :  ")
        while subject_name.isdigit():
            subject_name = input("Subject name cannot be a number. Enter again: ")

        marks = input(f"Enter the marks obtained in {subject_name} : ")
        while not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
            marks = input("Enter valid marks(0 to 100): ")

        subject["subject_name"] = subject_name
        subject["marks"] = int(marks)
        subjects.append(subject)

    
    return subjects

    start()

def get_student_information():
    no_of_students = input("Enter number of students  ")
    while not no_of_students.isdigit() or int(no_of_students) <=0:
        no_of_students = input("Invalid. Please enter a valid number of students.")
    no_of_students = int(no_of_students)
    for student_index in range(0,no_of_students):
        student = {
            "student_name":"",
            "subjects":[],
            "average": 0
        }
        student_name = input(f"Enter the name of the student {student_index+1} ")
        while student_name.strip() == "" or student_name.isdigit():
            student_name = input("Invalid. Student name cannot be empty or a number. Enter again: ")
        print(f"The student name entered is {student_name}")
        student["student_name"] = student_name
        subjects = get_subject_information()
        student["subjects"] = subjects
        total = 0
        for subject in subjects:
            total = total + subject["marks"]
        average = total / len(subjects)
        student["average"] = round(average, 2)    
        students.append(student)
        
    start()

def display_students():
    print("The students are ", students)
    start()

def display_top_three_performers():
    print("\nTop 3 Performers:")
    sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)
    top_three = sorted_students[:3]

    for i, student in enumerate(top_three, start=1):
        print(f"{i}. {student['student_name']} - Average: {student['average']}")
    start()

def display_students_above_threshold():
    threshold = 80
    print("\nStudents above threshold:")
    above_threshold = list(filter(lambda s: s["average"] > threshold, students))

    if above_threshold:
        for student in above_threshold:
            print(f"{student['student_name']} - Average: {student['average']}")
    else:
        print("No students found above the threshold.")
    start()


def choose_option():
    options = """Welcome to School Admin Software. Choose from below options
    1 - Enter student information
    2 - Display all the students
    3 - Top 3 performers (average)
    4 - Find students above threshold
    5 - exit
    """
    return input(options)

def go_to_option(selected_option):
    if selected_option == "1":
        get_student_information()
    elif selected_option == "2":
        display_students()
    elif selected_option == "3":
        display_top_three_performers()
    elif selected_option == "4":
        display_students_above_threshold()
    elif selected_option == "5":
        exit()
    else:
        exit()

def start():
    selected_option = choose_option()
    print(f"The selected option is {selected_option}")
    go_to_option(selected_option)

start()