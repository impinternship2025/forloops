class User:
    borrowed_books = []
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        # self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        #Find  and remove
        self.borrowed_books.remove(book)
        