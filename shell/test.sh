#!/usr/bin/bash

echo $(which bash)

# $() is function or command exec
echo $(pwd)
pwd


name="kmp"
pass=123123

# variables print is $ or ${}
echo $name
echo "my name is ${name}"
printf "my name is %s\n" $name 

