class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def borrow_book(self, book_id, user_id):
        book_to_borrow = next(
            (book for book in self.books if book.id == book_id), None)
        user_borrowing = next(
            (user for user in self.users if user.id == user_id), None)

        if book_to_borrow and user_borrowing:
            if book_to_borrow.is_available:
                book_to_borrow.is_available = False
                print(
                    f"{user_borrowing.name} has borrowed '{book_to_borrow.title}'.")
            else:
                print(
                    f"Sorry, '{book_to_borrow.title}' is currently not available.")
        else:
            print("Book or user not found.")

    def return_book(self, book_id):
        book_to_return = next(
            (book for book in self.books if book.id == book_id), None)
        if book_to_return:
            if not book_to_return.is_available:
                book_to_return.is_available = True
                print(f"'{book_to_return.title}' has been returned.")
            else:
                print(f"'{book_to_return.title}' was not borrowed.")

# 1.- The system must allow to register books.(done in main.py)
# 2.- The system must allow to register users.(done in main.py)
# 3.- The system must allow a user to borrow a book. (done in library.py)
# 4.-A book that has already been borrowed cannot be borrowed again.
# 5.- The system must allow a book to be returned.
