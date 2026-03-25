n = int(input("Введите количество чисел (N): "))
current_num = float(input("Введите число 1: "))
max_num = current_num
for i in range(2, n + 1):
    current_num = float(input(f"Введите число {i}: "))
    if current_num > max_num:
        max_num = current_num
print(f"Максимальное число: {max_num}")
