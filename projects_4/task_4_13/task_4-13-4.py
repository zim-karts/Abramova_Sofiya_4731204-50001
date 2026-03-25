n = int(input("Введите натуральное число: "))
res = 1
for i in range(2, n + 1):
    res += i
print(f"Сумма первых натуральных N чисел: {res}")