//QUESTION 1
   ls -d /usr/lib/lib* | wc -w>../../home/dyrroth/Desktop/assignment_1/count

//QUESTION 2
   wc -w / .* |sort -gr |grep -v 'total' |grep -v '^wc' >list.txt

//QUESTION 3
   top -n 1 |grep root >processes.txt

//QUESTION 4

 cat sample.txt |tr " " "\n" |sort -bdf |uniq -ci >ans.txt

//QUESTION 5
 
 who -q >usercount.txt

//QUESTION 6
6a. df -h --total |grep total >rem_space.txt
6b.history

//QUESTION 7
 { touch a.txt b.txt
 gedit a.txt b.txt
 cat a.txt >>b.txt }

//QUESTION 8

// system commands

ifconfig
mkdir
who
whoami
find
ls
dd
grep
chmod
gzip


//process control commands
df
free
top
kill
nice
fg



//utility commands
which
man
sudo
su


//QUESTION 9

grep a sample.txt | grep e sample.txt | grep i sample.txt | grep o sample.txt | grep -o u sample.txt | wc -l >aeiou_count.txt

//QUESTION 10

sort --uniq in.txt >out.txt

//QUESTION 11

 ls -S|grep ".conf$"|head -n 5 >../home/dyrroth/Desktop/larg.txt

//QUESTION 12

ls |grep 'linux' |grep -v 'unix' |wc -l >ans.txt

//QUESTION 13

 touch sample.txt command.txt
 grep -i unix sample.txt
 grep -i unix sample.txt >ans.txt

//QUESTION 14
 grep -o UNIX sample.txt |wc -l >ans.txt
