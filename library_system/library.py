from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self):
        title = input("Enter book title: ")
        while title == "" or title.isdigit():
            title = input("Invalid. Book title cannot be empty or a number: ")

        author = input("Enter author name: ")
        while author == "" or author.isdigit():
            author = input("Invalid. Author name cannot be empty or a number: ")

        isbn = input("Enter book ISBN: ")
        while isbn == "":
            isbn = input("Invalid. ISBN cannot be empty: ")

        self.books.append(Book(title, author, isbn))
        print(f"Book '{title}' added.\n")
        self.start()

    def register_user(self):
        user_id = input("Enter user ID: ")
        while user_id == "":
            user_id = input("Invalid. User ID cannot be empty: ")

        name = input("Enter user name: ")
        while name == "" or name.isdigit():
            name = input("Invalid. User name cannot be empty or a number: ")

        self.users.append(User(user_id, name))
        print(f"User '{name}' registered.\n")
        self.start()

    def lend_book(self):
        user_id = input("Enter user ID: ")
        user = None
        for user_item in self.users:
            if user_item.user_id == user_id:
                user = user_item
                break
        if not user:
            print("User not found.")
            return self.start()

        isbn = input("Enter ISBN of book to lend: ")
        book = None
        for book_item in self.books:
            if book_item.isbn == isbn:
                book = book_item
                break
        if not book:
            print("Book not found.")
            return self.start()

        if not book.available:
            print("Book is already borrowed.")
        elif book in user.borrowed_books:
            print("You already borrowed this book.")
        else:
            book.available = False
            user.borrowed_books.append(book)
            print(f"{book.title} has been lent to {user.name}.")
        self.start()

    def return_book(self):
        user_id = input("Enter user ID: ")
        user = None
        for u in self.users:
            if u.user_id == user_id:
                user = u
                break
        if not user:
            print("User not found.")
            return self.start()

        isbn = input("Enter ISBN of book to return: ")
        book_to_return = None
        for b in user.borrowed_books:
            if b.isbn == isbn:
                book_to_return = b
                break

        if book_to_return:
            book_to_return.available = True
            user.borrowed_books.remove(book_to_return)
            print(f"Book '{book_to_return.title}' returned.")
        else:
            print("Book not found in borrowed list.")
        self.start()

    def display_available_books(self):
        print("\nAvailable Books:")
        found = False
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
                found = True
        if not found:
            print("No available books.")
        self.start()

    def display_user_borrowed_books(self):
        user_id = input("Enter user ID: ")
        user = None
        for u in self.users:
            if u.user_id == user_id:
                user = u
                break
        if not user:
            print("User not found.")
            return self.start()

        print(f"\n{user.name}'s Borrowed Books:")
        if not user.borrowed_books:
            print("No books borrowed.")
        else:
            for book in user.borrowed_books:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")
        self.start()

    def choose_option(self):
        options = """
========== Library Management ==========
1. Add a Book
2. Register User
3. Lend Book
4. Return Book
5. View Available Books
6. View User Borrowed Books
7. Exit
"""
        return input(options)

    def go_to_option(self, option):
        if option == "1":
            self.add_book()
        elif option == "2":
            self.register_user()
        elif option == "3":
            self.lend_book()
        elif option == "4":
            self.return_book()
        elif option == "5":
            self.display_available_books()
        elif option == "6":
            self.display_user_borrowed_books()
        elif option == "7":
            print("Exiting from the system.")
            exit()
        else:
            print("Invalid choice.")
            self.start()

    def start(self):
        option = self.choose_option()
        self.go_to_option(option)

