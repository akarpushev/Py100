def generate_even_squares(n):
    """
    Функция для генерации списка квадратов четных чисел от 0 до N.
    """
    num = list[0:n]
    if n % 2 == 0:

        even_squares = [num ** 2]
        return even_squares



    # TODO Замените на list comprehension c условием фильтрации
    #even_squares = []
    #for i in range(n+1):
        #if i % 2 == 0:
            #even_squares.append(i**2)
    #return even_squares


print(generate_even_squares(5))  # [0, 4, 16]
print(generate_even_squares(10))  # [0, 4, 16, 36, 64, 100]
print(generate_even_squares(0))  # [0]


# Пример 1: Умножение каждого элемента списка на 2
numbers = [1, 2, 3, 4, 5]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)

# Пример 2: Фильтрация положительных чисел
numbers = [1, -2, 3, -4, 5]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)
