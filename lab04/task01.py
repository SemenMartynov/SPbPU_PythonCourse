import json

INPUT_FILE = "input.json"


# TODO решите задачу
def task() -> float:
    """
    Функция читает JSON файл и ищет сумму произведений двух значений в каждом словаре
    """
    with open(INPUT_FILE) as file:
        data = json.load(file)

    # Вычисляем произведение "score" * "weight" в каждом словаре
    # и находим сумму этих произведений
    accumulator = sum(record["score"] * record["weight"] for record in data)

    # Возвращаем значение с плавающей запятой, округленное до 3 знаков
    return round(accumulator, 3)


print(task())
