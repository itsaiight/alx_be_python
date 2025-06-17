class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size = int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.__class__.__name__}: {book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' not found.")

    def return_book(self, book):
        self.add_book(book)
        print(f"Returned: {book.title}")

