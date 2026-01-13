def find_common_participants(str_1, str_2, ras=','):
    group = list()
    list_first_group = str_1.split(ras)
    list_second_group = str_2.split(ras)
    for i in list_first_group:
        for j in list_second_group:
           if i == j:
               group.append(i)
    return sorted(group)

    # TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group, '|'))