#!/usr/bin/bash


file1=${1}
file2=${2}

# -a , && 는 and
if [ -f ${file1} -a -f ${file2} ]; then
	echo "file1 and fil2 are file"
fi

if [ -f ${file1} ] && [ -f ${file2} ]; then
	echo "file1 and file2 are file"
fi

# -o || 는 or

if [ -f ${file1} -o -f ${file2} ]; then
	echo "file1 or file2 are file"
fi

if [ -f ${file1} ] || [ -f ${file2} ]; then
	echo "file1 or file2 are file"
fi

