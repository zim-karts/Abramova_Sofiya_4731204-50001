import pandas as pd

df = pd.read_csv('wild_boars.csv')

cv_results = []

male_data = df[df['gender'] == 'Male']['tusk_length_cm']
female_data = df[df['gender'] == 'Female']['tusk_length_cm']

def calculate_cv(data):
    mean = data.mean()
    std_dev = data.std()
    if mean == 0:
        return 0
    return (std_dev / mean) * 100

male_cv = calculate_cv(male_data)
cv_results.append(f"Самцы: Коэффициент вариации длины клыков = {male_cv:.2f}%")

female_cv = calculate_cv(female_data)
cv_results.append(f"Самки: Коэффициент вариации длины клыков = {female_cv:.2f}%")

with open('cv_tusk_length.txt', 'w', encoding='utf-8') as file:
    file.write("Коэффициент вариации длины клыков по полу:\n")
    for line in cv_results:
        file.write(line + '\n')

print("Коэффициент вариации длины клыков по полу:")
for line in cv_results:
    print(line)