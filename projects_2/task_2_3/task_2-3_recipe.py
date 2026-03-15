nutrient_medium_name = input("Введите название питательной среды: ").strip().upper()
agar_concentration = input("Введите концентрацию агара (%): ").strip()
temperature = input("Введите температуру стерилизации (°C): ").strip()
print("Данные успешно сохранены в файл recipe.txt")
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"{nutrient_medium_name}\nКонцентрация агара: {agar_concentration} %\nТемпература стерилизации: {temperature} °C")