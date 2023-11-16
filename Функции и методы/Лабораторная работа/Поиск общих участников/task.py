# TODO Напишите функцию find_common_participants

def func (a, b):
    x = set(a.split('|'))
    y = b.split('|')
    list = sorted(x.intersection(y))
    return list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

list = func(participants_first_group, participants_second_group)
print(list)
