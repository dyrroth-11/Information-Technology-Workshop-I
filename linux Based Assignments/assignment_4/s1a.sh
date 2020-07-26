#!bin/bash
read str
sed -n "/${str}/p" s1b.txt | bash >s1c.txt
