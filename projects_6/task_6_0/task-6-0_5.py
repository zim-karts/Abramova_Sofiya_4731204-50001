import pandas as pd

df = pd.read_csv('wild_boars.csv')

percentiles_list = []

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

percentiles = {
    '25%': 0.25,
    '50%': 0.50,
    '75%': 0.75,
    '10%': 0.10,
    '90%': 0.90,
    '95%': 0.95,
    '5%': 0.05
}

for column in numeric_columns:
    for percentile_name, percentile_value in percentiles.items():
        value = df[column].quantile(percentile_value)
        result_line = f"{column} ({percentile_name}): {value:.2f}"
        percentiles_list.append(result_line)

with open('percentiles.txt', 'w', encoding='utf-8') as file:
    file.write("Процентили по параметрам:\n")
    for line in percentiles_list:
        file.write(line + '\n')

print("Процентили по параметрам:")
for line in percentiles_list:
    print(line)
