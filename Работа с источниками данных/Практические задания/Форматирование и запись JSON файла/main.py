import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
        result = [item["score"] * item["weight"] for item in data]
        return round(sum(result), 3)


        
    ...  # TODO Десериализуйте содержимое файла из переменной INPUT_FILE

    ...  # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
