# TODO Напишите функцию для поиска индекса товара
def get_id_by_name(items, item):
    """
    Функция для поиска индекса первого вхождения элемента в списке товаров.
    """
    for key, val in enumerate(items):
        if val == item:
            return key
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = get_id_by_name(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
