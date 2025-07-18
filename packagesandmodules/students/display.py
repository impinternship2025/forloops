from students.data import students

def display_students():
    print("\nStudent Subject-Wise Marks:")
    for student in students:
        print(f"\nStudent: {student['student_name']}")
        for subject in student['subjects']:
            print(f" {subject['subject_name']}: {subject['marks']}")
        print(f"  Average: {student['average']}")

def display_top_three_performers():
    print("\nTop 3 Performers")
    sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)
    top_three = sorted_students[:3]
    for i, student in enumerate(top_three, start=1):
        print(f"{i}. {student['student_name']} - Average: {student['average']}")

def display_students_above_threshold():
    threshold = 80
    print(f"\nStudents with average above {threshold}:")
    above_threshold = list(filter(lambda s: s["average"] > threshold, students))
    if above_threshold:
        for student in above_threshold:
            print(f" {student['student_name']} - Average: {student['average']}")
        else:
            print("No students found above threshold.")
            
                

