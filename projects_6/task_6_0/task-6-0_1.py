import pandas as pd

df = pd.read_csv('wild_boars.csv')

print("Длина клыков кабанов:")
print(df['tusk_length_cm'])

min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()

print("\nСамая короткая длина клыка:", min_tusk, "см")
print("Самая длинная длина клыка:", max_tusk, "см")