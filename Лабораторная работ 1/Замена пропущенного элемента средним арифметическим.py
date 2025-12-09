numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_without_None = numbers[:4]+numbers[5:]
# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = round(sum(numbers_without_None)/len(numbers), 2)
print("Измененный список:", numbers)
