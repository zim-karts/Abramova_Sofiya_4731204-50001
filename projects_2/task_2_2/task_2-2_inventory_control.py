with open ("inventory.txt", "w", encoding="utf-8") as fi:
    reagent_name = input("Введите название реагента: ").strip()
    number = input("Введите количество реагента: ").strip()
    fi.write(f"Реактив {reagent_name} поступил на склад в количестве {number} шт.")
