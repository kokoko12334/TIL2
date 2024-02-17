# !/usr/bin/bash

#대괄호
count=0
while [ ${count} -le 5 ];
do
	echo ${count}
	count=$((${count}+1))
done


#이중괄호


count=0
while (( ${count} <= 5));
do
	echo ${count}
	count=$((${count}+1))
done








