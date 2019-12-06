#!/bin/bash

echo "#include <stdio.h>
int main(void) {
	float n = $1;
	float j = 0;
	while (n != j) {
		printf(\"La note C : \");
		scanf(\"%f\",&j);
		if (j > n) printf(\"Et non C moins :)\n\");
		if (j < n) printf(\"Et non C plus :)\n\");
	}
	printf(\"C bien C ça :)\n\");
	return 0;
}" > devineNote-$2.c
gcc -Wall devineNote-$2.c -o devineNote-$2
echo "À table, C compilé !"
rm devineNote-$2.c
