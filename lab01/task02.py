# TODO Найдите количество книг, которое можно разместить на дискете

DISK_SIZE = 1.44 * 1024 * 1024

B_PAGES = 100
B_LINES = 50
B_SYMBOLS = 25
B_CHAR = 4

book_size = B_CHAR * B_SYMBOLS * B_LINES * B_PAGES

dick_capacity = int(DISK_SIZE / book_size)


print("Количество книг, помещающихся на дискету:", dick_capacity)
