from students.studentsubjectinfo import get_student_information
from students.display import (
    display_students,
    display_top_three_performers,
    display_students_above_threshold
)

def choose_option():
    options = """
Welcome to School Admin Software. Choose an option:
1 - Enter student information
2 - Display all students
3 - Top 3 performers (average)
4 - Find students above threshold
5 - Exit
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
        print("Exiting the program.")
        exit()
    else:
        print("Invalid option. Try again.")

def start():
    while True:
        selected_option = choose_option()
        print(f"You selected option {selected_option}")
        go_to_option(selected_option)
