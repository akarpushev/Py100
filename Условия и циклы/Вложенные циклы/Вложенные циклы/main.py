field = [  # поле 3x3 с крестиками и ноликами
    ["X", "O", "X"],  # первая строка таблицы
    ["O", "X", "O"],  # вторая строка таблицы
    ["X", "O", "X"],  # третья строка таблицы
]

for row in field:
    for cell in row:
        print(cell, end=" ")
    print()
