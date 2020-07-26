1.  ls -lR | grep '^-' | sort -k 5 -rn
           OR
ls -lS | grep '^-'	

2.  $* $@  
    uname -a
      OR 
  lscpu|grep'bit'

3.	ls -d /../usr/lib/lib* >

4.  cd /home
    sudo mkdir test
    cd test/
    sudo gedit new.txt
    mv new.txt ../../usr/lib
    cd ../../usr/lib
    sudo cat new.txt
    sudo rm new.txt
    cd home/
    sudo rmdir test
    
5.	bc -l > result.txt
	5 + 4
	6 - 8
	5 / 20
	4 * 19
	quit
	cat result.txt

6.  sudo shutdown -r +15

7.  export LS_COLORS="di=97;104:fi=31;42"
    ls 

8.  cmp xaa xab // compares byte by byte
	diff xaa xab  // compares line by line 

9.  grep -v "^#" sample.txt | grep -v "^'" | grep -v "^//"   // ^ denotes the lines starting with

10. awk '$1>= 000 && $1<= 999 { count++ } END { print count ? count : 0 }' sample.txt


11. grep -E 'a.a|e.e|i.i|o.o|u.u' sample.txt

12. ps -eo pid,lstart,time // pid process id, lstart is date and time of start,elapsed time of process //

13. pkill process_name

14. chmod 400	  222		010		777 file_name

15. chmod 466 file_name			touch file_name
								chmod 444 file_name

16. cat a1.txt | head -3 | tail -1

17. date | tee a1.txt  a2.txt a3.txt             ls -a | grep .*

18. ls | grep -v july 

19. grep word -m 2 sample.txt

20. wc -c a1.txt > out.txt