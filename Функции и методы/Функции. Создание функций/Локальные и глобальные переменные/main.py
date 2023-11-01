PI = 3.1415  # Константное значение
r = int(input())

def calculate_circumference(r):
    return 2 * PI * r
circumference = calculate_circumference(r)

def calculate_area(r):
    return PI * r ** 2

area = calculate_area(r)

print(circumference)
print(area)

