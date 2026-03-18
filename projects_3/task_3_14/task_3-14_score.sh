#!/bin/bash

awk '{

    if ($2 > 80)

        print $1

}' students.txt

awk '{

    if ($2 < 70)

        print $1

}' students.txt

awk 'NR==1' students.txt
