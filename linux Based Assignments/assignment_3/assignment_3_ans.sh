//QUESTION 1

1a. uptime -p
1b. passwd {user} -S

//QUESTION 2

2a. {
#!/bin/bash
#
echo "Current date and time is `date`"
echo "User is `whoami` "
echo "Current direcotry `pwd`"

}
 chmod +x s2.sh
 ./s2.sh

//QUESTION 3

3a. bc < s3.txt
    cat s3.txt
3b. seq 1 9
    or
    echo -e "1\n2\n3\n4\n5\n6\n7\n8\n9"

//QUESTION 4

4a. ps axjf
4b. ps -eo pid,time

//QUESTION 5
 . output of ps -t /dev/console is  { PID TTY     TIME CMD }

//QUESTION 6
{
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
}
//QUESTION 7
{
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
}

//QUESTION 8
{
	#!/bin/bash

read fname
if [ -d "$fname" ]
   then 
     cd $fname
elif [ -f "$fname" ]
   then 
     cat $fname
else
   echo " No such file or directory exist"
fi
ls -l | grep "^-rw*"
}

//QUESTION 9

{
	#!/bin/bash
read string
len=${#string}
k=$(($len/2))
ans=1
for (( i = 0; i < k; i++ ))
   do
	back=$(($len-$i-1))
	if [[ ${string:$i:1} != ${string:$back:1} ]]
            then
		ans=0
		break
 fi
done
 if [ $ans -eq 1 ]
     then
	echo "String ${string} is a palindrome."
 else
	echo "String ${string} is not a palindrome."
 fi
}
//QUESTION 10
{
	#!/bin/bash
read n

a=$(($n%4))
if [ $a -eq 0 ]
    then
	b=$(($n%100))
	if [ $b -eq 0 ]
             then
		c=$(($n%400))
		if [ $c -eq 0 ]
                   then

			echo "It's a leap year"
		else
			echo "No it's not a leap year"
		 fi
		
	else
		echo "It's a leap year "
	 fi
	
else
	echo "No it's not a leap year"
fi
}

//QUESTION 11
{
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
}
//QUESTION 12
{
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

}
//QUESTION 13

 pwgen 8 1

 //QUESTION 14
 sed '/^$/d' {file_name}

 //QUESTION 15

 ls -l  | sort -h -k 5
     OR
ls -lh | sort -h

//QUESTION 16

{
	#!/bin/bash
function area(){
 x=$1
 y=$2
 k=$(($1*$2))
return $k

}

read -p "Enter length of sides of rectangle" n m
 area $n $m
echo  " Area of rectangle is  $? "
}