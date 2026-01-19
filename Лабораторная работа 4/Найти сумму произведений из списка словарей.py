import json
# TODO решите задачу
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    sum_ = 0.0
    for item in data:
        score = item['score']
        weight = item['weight']

        sum_ += score*weight

    return round(sum_, 3)


print(task())
