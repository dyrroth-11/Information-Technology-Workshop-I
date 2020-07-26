//QUESTION 1
sh s1a.sh 
ls -l

//QUESTION 2
 2a. sed '1,100 s/gum/drum/g' s2.txt
 2d. sed 's/apple mango/mango apple/g' s2.txt 
 2c. sed '5 s/[0-9]*//' s2.txt

//QUESTION 3

. sed 's/\(^\|[^0-9.]\)\([0-9]\+\)\([0-9]\{3\}\)/\1\2,\3/g'
//QUESTION 4

. sed 's/\([^:]*\).*/\1/' /etc/passwd
//QUESTION 5

. sed -e  '1d' -e'$d' -e  '/^$/d' s5.txt

//QUESTION 6

. awk '{if(NF < 5 && NR > 1 ) print "Not all marks are available for",$1;}' student_marks.txt

//QUESTION 7

 awk ' {
 
avg = ($3 + $4 + $5) / 3
if (avg < 50)
    print $1,$2,$3,$4,$5 ": FAIL"
else if (avg < 60)
    print $1,$2,$3,$4,$5 ": C"
else if (avg < 80)
    print $1,$2,$3,$4,$5 ": B"
else
    print $1,$2,$3,$4,$5 ": A" }' student_marks.txt

//QUESTION 8

awk 'NR % 4 !=0 {printf $0;printf ","} NR % 4 ==0 {print " "}' s8.txt

//QUESTION 9

awk 'BEGIN {
   for (i = 1; i <= 10; ++i) {
      if (i == 5) continue;
      else  print i ;
   } 
}'

//QUESTION 10

awk -F' ' '{print NF}' student_marks.txt 

//QUESTION 11

. cat s11.txt | tr ';' ' ' | cut -d' ' -f'1,3,4'

//QUESTION 12

grep "/bin/bash" /etc/passwd | cut -d':'  -s -f1,6,7 --output-delimiter='#'

//QUESTION 13

. cat s13.txt | tr -s '[a-z];[A-Z];[0-9];[:space:]' | tr -d 'a'

//QUESTION 14

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
//QUESTION 15

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

//QUESTION 16

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

//QUESTION 17

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

//QUESTION 18

grep "/bin/bash" /etc/passwd | cut -d':'  -s -f1,6,7 --output-delimiter='#'

//QUESTION 19

19a. sed '/^$/ p' s19.txt
19b. sed -e '1d' -e'4d' s19.txt

//QUESTION 20

20a. sed -ne '1p' -e '$p' s20.txt
20b. sed -n '/unix/ !p ' s20.txt

//QUESTION 21
grep "os" s21.txt | sed 's/linux/unix/g'



amitbiswas.rs.cse17@iitbhu.ac.in