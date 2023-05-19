#!/bin/bash

input=`cat mots.txt | grep 'Entr' | tail -1 | cut -c 12- | tr -d '\r' | tr -d '}'`

./result.py $input