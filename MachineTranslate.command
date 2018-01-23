#!/bin/bash
cd $"$(dirname $0)"

sourcefile=""
while true
do
	echo "*********************************************************"
	if [ "$sourcefile" != "" ]
	then
		read -p "*** continue > ${sourcefile} (y/n?):" -n 1 iscontinue
		if [ "$iscontinue" = "y" ]
		then
			python3 pdf2txt.py $sourcefile
		else
			sourcefile=""
		fi
	else
		echo "you can pull txt or pdf into here！eg: /Users/huangtianning/Downloads/xx.txt(xx.pdf) .. (only one)"
		read -p "*** please input:" sourcefile
		python3 pdf2txt.py $sourcefile
	fi
done



