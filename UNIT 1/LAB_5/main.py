from books import book
from users import user
from library import library

library1 = library()
# Create instances of the classes
book1 = book("001", "OOP fundamentals", "Ana Sanchez", "E.A")
book2 = book("002", "Harry Potter", "J.K. Rowling", "Bloomsbury")

user1 = user("001", "Sebastian")
user2 = user("002", "Kelsy")


library1.add_book(book1)
library1.add_book(book2)
library1.add_user(user1)
library1.add_user(user2)

library1.show_books()

library1.borrow_book("002", "001")
library1.return_book("002")
