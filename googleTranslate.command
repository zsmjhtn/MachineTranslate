#!/bin/bash
cd $"$(dirname $0)"

sourceTxt=""
while true
do
	echo "*********************************************************"
	if [ "$sourceTxt" != "" ]
	then
		read -p "*** continue > ${sourceTxt} (y/n?):" -n 1 iscontinue
		if [ "$iscontinue" = "y" ]
		then
			python3 translate.py $sourceTxt
		else
			sourceTxt=""
		fi
	else
		echo "你可以拖入待翻译的英文txt到这里噢！eg: /Users/huangtianning/Downloads/xx.txt .. (only one)"
		read -p "*** please input:" sourceTxt
		python3 translate.py $sourceTxt
	fi
done



