# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r') as csvFile:
        data = [line for line in csv.DictReader(csvFile)]
    # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, mode='w') as jsonFile:
        json.dump(data, jsonFile, indent=4)
    # TODO Сериализовать в файл с отступами равными 4




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
