numbers = input("Введите натуральные числа через пробел: ").split()
array = [int(i) for i in numbers]
n = len(array)
res = 0
for i in range(n):
    res += array[i]
print(res)