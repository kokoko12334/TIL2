#!/usr/bin/bash


#expr``
declare -i num1
declare -i num2  #no need to
num1=10
num2=20

echo $num1
echo $num2

#expr ` `으로 수행, 이떄 연산자와 피연산자(숫자)는 띄어쓰여야한다.
plus=`expr $num1 + $num2`
minus=`expr $num1 - $num2`
mul=`expr $num1 \* $num2` #곱하기는 무조건 \*임
div=`expr $num1 / $num2`
rem=`expr $num1 % $num2`

result=`expr \( 3 \* 5 \) / \( 1 + 2 \)` #괄호 ()는 이스케잎써야함 무조건 띄어씌어야함

echo "plus: ${plus}"
echo "minus: ${minus}"
echo "mul: ${mul}"
echo "div: ${div}"
echo "rem: ${rem}"
echo "result: ${result}"



#let
#let은 피연산자 사이에 붙혀야함
let re=num1+num2
echo "add: ${re}"

let re=num1-num2
echo "sub: ${re}"

let re=num1*num2
echo "mul: ${re}"

let re=num1/num2
echo "div: ${re}"

let re=num1%num2
echo "mod: ${re}"


# $(()) 연산자
#이 연산자는 피연산자 사이에 띄어써도 되고 안 띄어써도됨
echo add: $((num1+ num2))
echo sub: $((num1 -num2))
echo mul: $((num1 * num2))
echo div: $((num1/num2))
echo mod: $((num1%num2))



