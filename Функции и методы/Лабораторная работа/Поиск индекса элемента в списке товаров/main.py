# TODO Напишите функцию для поиска индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def func(a, b):
    if b in a:
        index_item = items_list.index(find_item)
    else:
        index_item = None
    return index_item



for find_item in ['банан', 'груша', 'персик']:
    index_item = func(items_list, find_item)
    ...  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
