#!/bin/bash

echo "ESPEAK !!!"
while true; do
read -rsn1 input
if [ "$input" != "" ]; then espeak "$input";fi
done