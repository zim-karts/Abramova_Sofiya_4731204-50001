read -p "Введите ваш вес: " weight
read -p "Введите ваш рост: " height_cm

# Перевод роста в метры
height_m=$(echo "scale=2; $height_cm / 100" | bc)

# Расчет ИМТ (кг/м^2)
bmi=$(echo "scale=2; $weight / ($height_m * $height_m)" | bc)

echo "Ваш ИМТ: $bmi"
