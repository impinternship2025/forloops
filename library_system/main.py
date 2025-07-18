from library import Library

def show_menu():
    print("""
=========  Library Menu =========
1. Add Book
2. View Books
3. Add New User
4. Register New User
5. Lend Book
6. Return Book
7. Exit
""")

def start():
    lib = Library()

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            isbn = input("Enter Book ISBN: ")
            lib.add_book(title, author, isbn)

        elif choice == "2":
            lib.view_books()

        elif choice == "3":
            user_id = input("Enter New User ID: ")
            name = input("Enter User Name: ")
            lib.add_user(user_id, name)

        elif choice == "4":
            user_id = input("Enter User ID to Register: ")
            name = input("Enter User Name: ")
            lib.register_user(user_id, name)

        elif choice == "5":
            isbn = input("Enter ISBN to Lend: ")
            user_id = input("Enter User ID: ")
            lib.lend_book(isbn, user_id)

        elif choice == "6":
            isbn = input("Enter ISBN to Return: ")
            user_id = input("Enter User ID: ")
            lib.return_book(isbn, user_id)

        elif choice == "7":
            print(" Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 7.\n")

start()
