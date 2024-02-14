class Book:
    """
    Базовый класс, представляющий книгу.

    Атрибуты:
    name (str): Название книги (приватный атрибут).
    author (str): Автор книги (приватный атрибут).
    """

    def __init__(self, name: str, author: str):
        """
        Конструктор класса.

        Параметры:
        name (str): Название книги.
        author (str): Автор книги.
        """
        self.__name = name
        self.__author = author

    def __str__(self):
        """
        Метод для строкового представления объекта класса.

        Возвращает:
        str: Строка в формате "Книга {название}. Автор {автор}".
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Метод для формального строкового представления объекта класса.

        Возвращает:
        str: Строка в формате "Book(name={название}, author={автор})".
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """
        Свойство для получения названия книги.

        Возвращает:
        str: Название книги.
        """
        return self.__name

    @property
    def author(self) -> str:
        """
        Свойство для получения автора книги.

        Возвращает:
        str: Автор книги.
        """
        return self.__author


class PaperBook(Book):
    """
    Подкласс книги, представляющий бумажную версию книги.

    Атрибуты:
    pages (int): Количество страниц в книге.
    """

    def __init__(self, name: str, author: str, pages: int):
        """
        Конструктор класса.

        Параметры:
        name (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц в книге.
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """
        Метод для формального строкового представления объекта класса.

        Возвращает:
        str: Строка в формате "PaperBook(name={название!r}, author={автор!r}, pages={страницы!r})".
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        """
        Свойство для получения количества страниц.

        Возвращает:
        int: Количество страниц в книге.
        """
        return self.__pages

    @pages.setter
    def pages(self, value):
        """
        Метод для установки количества страниц.

        Параметры:
        value (int): Количество страниц в книге.

        Исключения:
        TypeError: Если 'value' не является целым числом.
        ValueError: Если 'value' меньше или равно 0.
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц имеет неправильный тип!")
        if value <= 0:
            raise ValueError("Количество страниц задано не верно!")
        self.__pages = value


class AudioBook(Book):
    """
    Подкласс книги, представляющий аудиокнигу.

    Атрибуты:
    duration (float): Продолжительность аудиокниги в часах.
    """

    def __init__(self, name: str, author: str, duration: float):
        """
        Конструктор класса.

        Параметры:
        name (str): Название аудиокниги.
        author (str): Автор аудиокниги.
        duration (float): Продолжительность аудиокниги в часах.
        """
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        """
        Метод для формального строкового представления объекта класса.

        Возвращает:
        str: Строка в формате "AudioBook(name={название}, author={автор}, duration={продолжительность})".
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        """
        Свойство для получения продолжительности аудиокниги.

        Возвращает:
        float: Продолжительность аудиокниги в часах.
        """
        return self.__duration

    @duration.setter
    def duration(self, value):
        """
        Метод для установки продолжительности аудиокниги.

        Параметры:
        value (float): Продолжительность аудиокниги в часах.

        Исключения:
        TypeError: Если 'value' не является int или float.
        ValueError: Если 'value' меньше или равно 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность имеет неправильный тип!")
        if value <= 0:
            raise ValueError("Продолжительность задана не верно!")
        self.__duration = value


if __name__ == '__main__':
    pb = PaperBook('name', 'author', 123)
    print(pb)
    print(repr(pb))
    ab = AudioBook('name', 'author', 12.3)
    print(ab)
    print(repr(ab))
