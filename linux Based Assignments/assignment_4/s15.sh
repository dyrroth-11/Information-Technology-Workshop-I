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
