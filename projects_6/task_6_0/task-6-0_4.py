import pandas as pd

df = pd.read_csv('wild_boars.csv')

modes_list = []

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    # Вычисляем моду для числовых столбцов
    mode_value = df[column].mode()[0]
    result_line = f"{column}: {mode_value:.2f}"
    modes_list.append(result_line)

for column in df.select_dtypes(exclude=['float64', 'int64']).columns:
    # Вычисляем моду для категориальных столбцов
    mode_value = df[column].mode()[0]
    result_line = f"{column}: {mode_value}"
    modes_list.append(result_line)

with open('modal_values.txt', 'w', encoding='utf-8') as file:
    file.write("Модальные значения по параметрам:\n")
    for line in modes_list:
        file.write(line + '\n')

print("Модальные значения по параметрам:")
for line in modes_list:
    print(line)