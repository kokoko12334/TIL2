#! /usr/bin/bash


declare -a arr #굳이 안써줘도 됨

arr=("t1" "t2" "t3")



#arr 추가 방법

arr[3]="t4"
arr+=("t5")

n=${#arr[@]}  #배열의 길이
echo ${n}
arr[n]="t6"



echo ${arr[0]} #index
echo ${arr[*]} #모든 데이터를 가져오는데 다 합침
echo ${arr[@]} #모든 데이터를 가져오는데 다 따로
echo ${arr[@]:2:3} #indexing


#삭제


arr=("a" "b" "c")

unset arr[1]
echo ${arr[@]}

unset arr #배열 자체를 삭제

