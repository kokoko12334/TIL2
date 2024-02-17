#!/usr/bin/bash

string=global_value
function string_test(){

	#지역변수 설정
	local string="local_value"
	echo $string


}
#함수 실행
string_test
echo $string

#reset
unset string
