#!/bin/bash

for i in {1..10}
do
    touch "file_$i.txt"
    echo "создан файл $i"
done

count=1
while [ $count -le 10 ]
do
    rm file_$count.txt
    echo "файл $count удален"
    ((count ++))
done
