# !/usr/bin/bash



#그냥 date 문자열 출력
echo date


#date 명령어 실행
echo `date`

#date 명령어 실행
echo $(date)



for file in `ls`
do
	echo $file
done

