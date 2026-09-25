class book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.title = name
        self.author = author
        self.editorial = editorial
        self.is_available = True

    def show_book_info(self):
        return f"{self.id} - {self.title} - {self.author}"
