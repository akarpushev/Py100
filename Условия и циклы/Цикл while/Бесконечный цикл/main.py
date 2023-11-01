total = 0

while True:
    number = int(input())

    if number > 10000:
        break

    total += int(number)  # Суммируем число с общей суммой

print("Сумма чисел:", total)  # Выводим общую сумму
print("Конец программы")
