#!/usr/bin/bash


for ((i=0; i<4; i++ )); do
	echo $i
done



#1
for x in 1 2 3 4 5
do
	echo ${x}
done


#2
data="1 2 3 4 5"
for x in $data
do
	echo ${x}
done

#3
arr=(1 2 3 4 5)
for i in "${arr[@]}"  #arr[@]: 배열 전체 출력
do
	echo ${i}
done


#sequence 를 이용한 for문
for num in `seq 1 5`
do
	echo $num
done

#range
for x in {1..10}
do
	echo $x
done



#역따옴표 써버 ls를 명령어를 수행한다.
arr=(`ls`,`pwd`)
for line in ${arr[@]}
do
	echo $line
done






