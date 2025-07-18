class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False
