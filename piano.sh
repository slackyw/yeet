#!/bin/bash

echo "LE PIANO DU YEET !!!"

declare -A idx=(['q']=0 ['s']=1 ['d']=2 ['f']=3 ['g']=4 ['h']=5 ['j']=6 ['k']=7 ['l']=8 ['m']=9)


declare -a octave0=("16,35" "17,33" "18,36" "19,45" "20,60" "21,83" "23,13" "24,50" "25,96" "27,50" "29,14" "30,87")

while true; do
read -rsn1 input
if [ "$input" != "" ];then
	echo ${octave0[${idx[$input]}]}
fi
done