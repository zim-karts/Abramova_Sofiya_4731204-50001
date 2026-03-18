#!/bin/bash

echo -e "Сумма оценок"
awk '{sum += $2} END {print sum}' students.txt

echo -e "\nСреднее арифметическое всех оценок"
awk '{sum += $2; n++} END {print sum/n}' students.txt

echo -e "\nМаксимальная оценка"
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
