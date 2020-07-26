#!/bin/bash
read -p "Enter number to be reversed " n
digit=0
rev=0
while [ $n -gt 0 ]
do
    digit=$(( $n % 10 ))
    rev=$(( $rev * 10 + $digit ))
    n=$(( $n / 10 ))
done
echo "Reverse number of entered digit is $rev"
