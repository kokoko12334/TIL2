# !/usr/bin/bash


declare -A map=([a]="hello" [b]="world")

declare -p map #map 출력

echo "a: ${map[a]}"
echo "b: ${map[b]}"

echo "values: ${map[@]}" #순서 보장 x
echo "key: ${!map[@]}" # 순서 보장 x
echo "length: ${#map[@]}"



#추가

map+=([c]="ccccc")
map+=([d]="dddd" [e]="eee")
map[f]="ffff"

echo "values: ${map[@]}"
echo "keys: ${!map[@]}"


#삭제

unset map[a]

echo "keys: ${!map[@]}"


#loop


for v in ${map[@]}
do
	echo ${v}
done

for k in ${!map[@]}
do
	echo ${k}
done







