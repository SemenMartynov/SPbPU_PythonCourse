numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

none_id = numbers.index(None)
#print(f"{none_id=}")

first_half = numbers[:none_id]
#print(f"{first_half=}")

last_half = numbers[none_id + 1:]
#print(f"{last_half=}")

summ = sum(first_half) + sum(last_half)
#print(f"{summ=}")

quant = len(numbers)
#print(f"{quant=}")

avg = summ / quant
#print(f"{avg=}")

new_numbers = first_half + [avg] + last_half
print("Измененный список:", new_numbers)
