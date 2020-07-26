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
