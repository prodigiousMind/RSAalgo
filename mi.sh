#!/bin/bash

n1=${1}
n2=${2}

function mmi(){
	for ((i=1;i<${n2};i++))
		do
			if [[ $(((i*${n1})%${n2})) -eq 1 ]]
				then echo "Modular Multiplicative Inverse of ${n1} mod ${n2} is ${i}"
				break
			fi
		done
}

if [[ $# -eq 0 ||  $# -gt 2 || "${n1}" == "help"  ]]
  then
    echo -e "Help:\nbash mi.sh [num1] [num2]"
else
	mmi
fi


