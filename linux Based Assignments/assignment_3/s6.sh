#!/bin/bash 
if [ $# -ne 2 ]
then
    echo " input correct numbers."
    exit 1
elif [ $1 -le 0 ]
then
    echo " input correct numbers."
    exit 1
elif [ $2 -le 0 ]
then
    echo " input correct numbers."
    exit 1
fi

if [ $1 -gt $2 ]
then 
 echo -n   " answer is "; echo  $2/$1 |bc -l

else 
  echo -n " answer is  $n2 ";  echo  $1/$2 |bc -l 

fi
