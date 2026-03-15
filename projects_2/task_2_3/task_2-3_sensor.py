name = input("Введите имя оператора: ").strip()
total = input("Введите показания датчика давления (Па): ").strip()
print("Данные успешно сохранены в файл sensor_log.txt")
with open("sensor_log.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}\t{total}")