#!/bin/bash

num=`cat innondation.txt | grep '> ' -n | cut -d ':' -f 1 | tail -2 | wc -l`

if [ "$num" = "1" ]
then
	cat innondation.txt | grep -o '~' | wc -l
else
	num=`cat innondation.txt | grep '> ' -n | cut -d ':' -f 1 | tail -2 | head -1`
	tail innondation.txt --lines=+${num} | grep -o '~' | wc -l
fi
