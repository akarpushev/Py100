INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as input_file:
        with open(OUTPUT_FILE, 'w') as output_file:
            for line in input_file:
                output_file.write(line.upper())

    ...  # TODO перезаписать содержимое одного файла в другой


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
