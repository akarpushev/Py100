sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]


def calculate_total_sales(sales_list):
    sales_list = sales_data[0]["quantity"] * sales_data[0]["price_per_unit"]
    return sales_list


print(sales_list)










#otal_sales = calculate_total_sales(sales_list) ...  # TODO Вызовете функцию calculate_total_sales и передайте в функцию значение переменной sales_data
#print(f"Общая стоимость проданных товаров: {total_sales}")
