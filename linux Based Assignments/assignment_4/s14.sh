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
