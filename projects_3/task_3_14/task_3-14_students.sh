#!/bin/bash
echo "Имена"
awk '{print $1}' students.txt

echo -e "\nОценки"
awk '{print $2}' students.txt

echo -e "\nСписок"
awk '{print NR, $1}' students.txt

