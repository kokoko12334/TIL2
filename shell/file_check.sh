#!/usr/bin/bash


path=${1}
path2=${2}
if [ -e ${path} ]; then echo "yes path"; fi


if [ ! -e ${path} ]; then echo "no path"; fi


if [ -r ${path} ]; then echo "can read"; fi

if [ -w ${path} ]; then echo "can write"; fi

if [ -x ${path} ]; then echo "can exec"; fi

if [ -s ${path} ]; then echo "size is greater than 0"; fi

if [ -L ${path} ]; then echo "symbolic link"; fi

if [ -S ${path} ]; then echo "this is socket type"; fi

if [ -f ${path} ]; then echo "정규 파일"; fi

if [ -c ${path} ]; then echo "문자장치"; fi

if [ -n ${path2} ]; then
	
	if [ ${path} -nt ${path2} ]; then echo "path1 is more recent than path2"; fi
	if [ ${path} -ot ${path2} ]; then echo "path1 is older than path2"; fi
	if [ ${path} -ef ${path2} ]; then echo "path1 is equal to path2"; fi
fi
