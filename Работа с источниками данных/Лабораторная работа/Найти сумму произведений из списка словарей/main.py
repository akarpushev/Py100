# TODO решите задачу
import json
FILE = "input.json"

def task() -> float:
    with open(FILE) as f:
        data = json.load(f)
        result = [item["score"] * item["weight"] for item in data]
        return round(sum(result), 3)



print(task())
