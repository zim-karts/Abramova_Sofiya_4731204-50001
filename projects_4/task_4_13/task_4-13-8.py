numbers = input("Введите числа через пробел: ").split()
array = [float(i) for i in numbers]
n = len(array)
cnt = 0

for i in range(n):
    if array[i] > 0:
        cnt += 1

print(f"Количество положительных чисел: {cnt}")