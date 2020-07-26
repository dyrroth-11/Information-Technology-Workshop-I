#!/bin/bash
function is_prime(){
	x=$1
	for (( i = 2; $((i*i))<= $x; i++ ))
              do
		k=$((x%i))
		if [ $k == 0 ]
                 then
			return 0
		fi
	done
	return 1
	
}
read -p "How many prime numbers:" n
cnt=0
num=2
while [ $cnt -lt $n ] 
         do
	is_prime "${num}"
	if [ $? -eq 1 ]
            then
		echo ${num}
		cnt=$(($cnt+1))
	fi
	num=$(($num+1))
done
