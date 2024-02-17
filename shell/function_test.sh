# /usr/bin/bash



#굳이 function, func를 쓸 필요는 없다.
#함수 호출시에 ()를 안쓷쓴다
#함수호출코드는 반드시 정의된 함수 뒤에 써야함

this_is_func(){

	echo "this_is_func()"
}


function this(){

	echo "var: ${1}" #첫번쨰 인자
	echo "vars: ${@}" #모든 인자

}

this_is_func

this "hello" "world"
