#!/bin/bash
echo "Товары"
awk -F "," '{print $2}' data.csv

echo -e "\nТовары стоимостью свыше 20-ти"
awk -F "," '{

    if ($3 > 20)

        print $2

}' data.csv

echo -e "\nСуммарная стоимость"
awk -F "," '{sum += $3} END {print sum}' data.csv
