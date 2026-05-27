import pandas as pd

df = pd.read_csv('wild_boars.csv')

averages = {}

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    avg_value = df[column].mean()
    averages[column] = f"{column}: {avg_value:.2f}"

result_df = pd.DataFrame(list(averages.items()), columns=['Параметр', 'Среднее значение'])

result_df.to_csv('average_values.csv', index=False, encoding='utf-8')

print("Средние значения по параметрам:")
print(result_df)