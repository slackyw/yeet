#!/bin/bash

echo "ABOUIBOUIBOUI !!!"
while true; do
read -rsn1 input
if [ "$input" == "a" ];then 
	espeak -v fr "a" &
fi
if [ "$input" == "b" ];then
	espeak -v fr "boui" &
fi
done