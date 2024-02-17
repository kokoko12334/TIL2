#!/usr/bin/bash



# if는 fi로 끝을 낸다. if[]와 그 사이들에는 띄어씌기를 해야한다.




if [ 10 -eq 10 ]; then
	echo "equal"
fi

if [ 10 -ne 20 ]; then
	echo "not equal"
fi

if [ 30 -gt 10 ]; then
	echo "30 is greater than 10"
fi

if [ 30 -ge 30 ]; then
	echo "30 is greater than or equal to 30"
fi

if [ 10 -lt 20 ]; then
	echo "10 is less than 20"
fi

if [ 10 -le 10 ]; then echo "10 is less than or equal to 10"; fi #one line




# (()) 표현법

num1=10
num2=20




if ((${num1} + ${num2} == 30)); then echo "yes"; fi



if (( (${num1} * ${num2}) > 10 )); then
	echo "greater than 10"
else
	echo "less than 10"
fi



