import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('wild_boars.csv')

# Создаем пустой список для хранения результатов
medians_list = []

# Проходим по каждому числовому столбцу
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    # Вычисляем медианное значение
    median_value = df[column].median()
    # Формируем строку с результатом
    result_line = f"{column}: {median_value:.2f}"
    # Добавляем в список
    medians_list.append(result_line)

# Записываем результаты в файл
with open('median_values.txt', 'w', encoding='utf-8') as file:
    file.write("Медианные значения по параметрам:\n")
    for line in medians_list:
        file.write(line + '\n')

# Выводим результат в консоль
print("Медианные значения по параметрам:")
for line in medians_list:
    print(line)