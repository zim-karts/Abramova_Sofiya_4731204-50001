numbers = input("Введите натуральные числа через пробел: ").split()
array = [float(i) for i in numbers]
n = len(array)
sum = 0

for i in range(n):
    if array[i]%2 != 0:
        sum += array[i]

print(f"Сумма нечетных чисел: {sum}")