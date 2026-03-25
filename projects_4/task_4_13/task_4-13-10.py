numbers = input("Введите натуральные числа через пробел: ").split()
array = [float(i) for i in numbers]
n = len(array)
sum = 0

for i in range(1, n, 2):
    sum += array[i]

print(f"Сумма чисел с нечетными индексами: {sum}")