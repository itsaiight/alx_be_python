class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size = int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count= int):
        super().__init__(title, author)
        self.page_count = page_count

class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"{book.__class__.__name__}: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"{book.__class__.__name__}: {book.title} by {book.author}, Page_count: {book.page_count}")
            else:
                print(f"{book.__class__.__name__}: {book.title} by {book.author}")



