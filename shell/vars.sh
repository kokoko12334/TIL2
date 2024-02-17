#!/usr/bin/bash

echo "script name:${0}"
echo "vars length:${#}"
echo "variables:${*}"  #변수를 하나의 문자열로 결합
echo "variables2:${@}" #변수들을 각자의 변수들로 즉, 독립적임.
echo "var1:${1}"
echo "var2:${2}"
echo "var3:${3}"
