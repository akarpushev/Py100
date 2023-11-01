count = 0
powerplants = [
    {"name": "ГЭС-1", "power": 1200},
    {"name": "АЭС-2", "power": 3200},
    {"name": "ТЭЦ-3", "power": 2800},
    {"name": "СГУ-4", "power": 500},
    {"name": "ВЭС-5", "power": 1800},
]
threshold_power = 2000

for i in range(len(powerplants)):
    a = powerplants[i]["power"]
    if a > threshold_power:
        count = count + 1

#print(count)
print(f"Количество электростанций, мощность которых превышает заданное значение: {count}")


#def count_powerful_powerplants(powerplants_list, threshold):
    #return count


#for i in range(len(powerplants)):
    #if powerplants[i]["power"] > threshold_power
    #count = count+1


#powerplants_count = count_powerful_powerplants(powerplants_list, threshold)

#print(f"Количество электростанций, мощность которых превышает заданное значение: {powerplants_count}")
