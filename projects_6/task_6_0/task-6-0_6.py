import pandas as pd

df = pd.read_csv('wild_boars.csv')

iqr_results = []

male_data = df[df['gender'] == 'Male']['length_cm']
female_data = df[df['gender'] == 'Female']['length_cm']

def calculate_iqr(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    return iqr

male_iqr = calculate_iqr(male_data)
iqr_results.append(f"Самцы: Межквартильный размах длины тела = {male_iqr:.2f} см")

female_iqr = calculate_iqr(female_data)
iqr_results.append(f"Самки: Межквартильный размах длины тела = {female_iqr:.2f} см")

with open('iqr_length.txt', 'w', encoding='utf-8') as file:
    file.write("Межквартильный размах длины тела по полу:\n")
    for line in iqr_results:
        file.write(line + '\n')

print("Межквартильный размах длины тела по полу:")
for line in iqr_results:
    print(line)
