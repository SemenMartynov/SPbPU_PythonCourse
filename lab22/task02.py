BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int) -> None:
        """Инициализирует экземпляр класса Book.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строку с описанием экземпляра книги.

        Returns:
            str: Строка формата "Книга "название_книги"".
        """
        return f"Книга \"{self.name}\""

    def __repr__(self) -> str:
        """Возвращает валидную строку Python для инициализации экземпляра книги.

        Returns:
            str: Строка формата "Book(id_=1, name='test_name_1', pages=200)".
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None) -> None:
        """Инициализирует экземпляр класса Library.

        Args:
            books (list): Список книг. По умолчанию создаётся пустой список.
        """
        self.books = books or []  # Если books не передан, инициализируем пустым списком

    def get_next_book_id(self) -> int:
        """Возвращает идентификатор для добавления новой книги в библиотеку.

        Returns:
            int: Идентификатор для следующей книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Возвращает индекс книги по идентификатору.

        Args:
            book_id (int): Идентификатор книги.

        Returns:
            int: Индекс книги в списке.

        Raises:
            ValueError: Если книги с запрашиваемым id не существует.
        """
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
