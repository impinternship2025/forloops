from user import User
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(" Book with this ISBN already exists.\n")
                return
        self.books.append(Book(title, author, isbn))
        print(" Book added successfully.\n")

    def view_books(self):
        if not self.books:
            print("No books available.\n")
            return
        print("\n Book List:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn}) - {status}")
        print()

    def add_user(self, user_id, name):
        for user in self.users:
            if user.user_id == user_id:
                print(" User already exists.\n")
                return
        self.users.append(User(user_id, name))
        print(" User added.\n")

    def register_user(self, user_id, name):
        for user in self.users:
            if user.user_id == user_id:
                print("User already registered.\n")
                return
        self.users.append(User(user_id, name))
        print(" User registered successfully.\n")

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def lend_book(self, isbn, user_id):
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)

        if not book:
            print(" Book not found.\n")
            return
        if not user:
            print(" User not found.\n")
            return
        if book.is_borrowed:
            print(" Book already borrowed.\n")
            return

        book.mark_as_borrowed()
        user.borrow_book(book.title)   
        print(f" {book.title} lent to {user.name}.\n")

    def return_book(self, isbn, user_id):
        book1 = self.find_book_by_isbn(isbn)
        user1 = self.find_user_by_id(user_id)

        if not book1 or not user1:
            print(" Invalid user or book.\n")
            return
        if book1.title not in user1.borrowed_books:
            print(f" {user1.name} has not borrowed {book1.title}.\n")
            return

        book1.mark_as_returned()
        user1.return_book(book1.title)   
        print(f" {user1.name} returned {book1.title}.\n")
