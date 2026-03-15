volume = input("Введите необходимый объем раствора (мл): ").strip()
NaCl_mass = int(volume)*0.009
water_volume = int(volume)
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n----------------------\nОбщий объем: \t{volume} мл\nМасса соли: \t{NaCl_mass:.2f} г\nОбъем воды: \t{water_volume} мл")