#!/bin/bash

# sudo apt install espeak beep -y;git clone "https://github.com/floriangarciasoto/ilestoumonprojet";cd ilestoumonprojet/;bash yeet.sh 60 "pikatchu, attak eclair" 3 20 300 2000

export DISPLAY=:0
amixer sset 'Master' unmute 1>/dev/null
amixer sset 'Master' $1% 1>/dev/null
espeak "$2"
outp=`xrandr | grep " con" | awk '{print $1}'`
for i in `seq 1 $3`
do
	xrandr --output $outp --gamma 0.$((RANDOM%9+1)):0.$((RANDOM%9+1)):0.$((RANDOM%9+1))
	sudo env -i beep -l $4 -f $((RANDOM%($6-$5)+$5))
done
xrandr --output $outp --gamma 1:1:1
