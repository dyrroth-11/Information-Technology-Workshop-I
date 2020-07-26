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
