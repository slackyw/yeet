#!/bin/bash

echo "LE PIANO DU YEET !!!"
while true; do
read -rsn1 input
if [ "$input" = "q" ]; then beep -l 150 -f 220;fi
if [ "$input" = "s" ]; then beep -l 150 -f 280;fi
if [ "$input" = "d" ]; then beep -l 150 -f 300;fi
if [ "$input" = "f" ]; then beep -l 150 -f 315;fi
if [ "$input" = "g" ]; then beep -l 150 -f 330;fi
if [ "$input" = "h" ]; then beep -l 150 -f 350;fi
if [ "$input" = "j" ]; then beep -l 150 -f 375;fi
if [ "$input" = "k" ]; then beep -l 150 -f 405;fi
if [ "$input" = "l" ]; then beep -l 150 -f 450;fi
if [ "$input" = "m" ]; then beep -l 150 -f 550;fi
done