#!/usr/bin/bash


#case는 이중 ;;으로 끝낸닫
case ${1} in

	"linux")
		echo "리눅스" ;;
	"unix")
		echo "유닉스" ;;
	"windows")
		echo "윈도우즈" ;;
	*) echo "나머지" ;;
esac
