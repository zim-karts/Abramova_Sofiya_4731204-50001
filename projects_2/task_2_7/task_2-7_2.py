seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
n = len(seq)
for i in range(n):
    print(seq[i])
    for letter in seq[i]:
        print(letter)
print("Цикл выполнен")