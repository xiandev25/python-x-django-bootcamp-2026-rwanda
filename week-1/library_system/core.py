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

    def __str__(self):
        return f"{self.name} has {len(self.books)} books"

    def __getitem__(self, index):
        return self.books[index]

    def __len__(self):
        return len(self.books)

    def __eq__(self, other):
        if isinstance(other, Library):
            return self.name == other.name and self.books == other.books
        return False