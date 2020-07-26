#!/bin/bash

function num(){
y=$1
csum=0
while [ $y -gt 0 ]
 do
 k=$(($y%10))
csum=$(($csum +k*k*k))
y=$(($y/10))
done
if [ $1 -eq $csum ]
then
  return 1
fi
 return 0
}

echo "Number whose sum of cube of digits equal to number itself : "

for (( i = 1 ; i < 1000 ;i++))
 do 
   num "${i}"
   if [ $? -eq 1 ]
 then 
    echo $i
  fi
done

