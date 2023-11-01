# TODO Вызовите ошибку AssertionError с собственным текстом
def multi(a, b) -> float:
    if a < 4:
        raise TypeError ('предупреждение')
    else:
        c = a * b
    return c



a, b = 5, 7.5
print(multi(a, b))
