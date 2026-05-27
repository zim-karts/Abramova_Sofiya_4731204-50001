import pandas as pd

df = pd.read_csv('wild_boars.csv')

stats_list = []

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

for column in numeric_columns:
    variance = df[column].var()
    std_dev = df[column].std()
    mean = df[column].mean()
    
    if mean != 0:
        coeff_var = (std_dev / mean) * 100
    else:
        coeff_var = 0

    stats_list.append(f"{column} - Дисперсия: {variance:.2f}")
    stats_list.append(f"{column} - Стандартное отклонение: {std_dev:.2f}")
    stats_list.append(f"{column} - Коэффициент вариации: {coeff_var:.2f}%")

with open('statistics.txt', 'w', encoding='utf-8') as file:
    file.write("Статистические показатели по параметрам:\n\n")
    for line in stats_list:
        file.write(line + '\n')

print("Статистические показатели по параметрам:")
for line in stats_list:
    print(line)
