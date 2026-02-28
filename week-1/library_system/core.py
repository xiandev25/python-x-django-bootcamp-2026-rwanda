class Book:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.page

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

class Library:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError(f"Book {book} not found in library {self.name}")

    def return_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"{self.name} has {len(self.books)} books"

    def __getitem__(self, index):
        try:
            return self.books[index]
        except IndexError:
            raise IndexError(f"Book at {index} not found")

    def __contains__(self, book):
        return book in self.books

    def __len__(self):
        return len(self.books)

    def __eq__(self, other):
        if isinstance(other, Library):
            return self.name == other.name and self.books == other.books
        return False