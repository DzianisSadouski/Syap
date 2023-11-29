class Book:
    books = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.books.append(self)

    def display_books(self):
        print("Список книг:")
        for book in Book.books:
            print(f"Название: {book.title}, Автор: {book.author}, ISBN: {book.isbn}")

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def create_book_from_string(cls, book_string):
        parts = book_string.split(";")
        if len(parts) == 3 and cls.is_valid_isbn(parts[2]):
            return cls(parts[0], parts[1], parts[2])
        else:
            print("Неверный формат строки. Книга не создана.")
            return None

book1 = Book("Война и мир", "Лев Толстой", "9781234567890")
book2 = Book("Преступление и наказание", "Федор Достоевский", "9789876543210")

book1.display_books()

book_string = "Мастер и Маргарита;Михаил Булгаков;9781122334455"
new_book = Book.create_book_from_string(book_string)

if new_book:
    new_book.display_books()
