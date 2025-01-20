#!/bin/bash

type_of_instance=$1
available_balance=$2
if [[ $type_of_instance == "t2.micro" && $available_balance -eq 10 ]]
then
    echo "we can create $1 instance"
else
    echo "we can't create the $1 instance"
fi

#for integer comparition,use the letter for relation operator(gt,lt,eq,ne etc)

cpu_usage=90
memory_usage=80

if [[ $cup_usage -ge 90 && $memory_usage -ge 80 ]]
then
   echo 'Server need the attention'
elif [[ $cup_usage -ge 80 && $memory_usage -ge 70 ]]
then
   echo 'server cpu usage is 80 or above and memory usage is 70 or more'
else
   echo 'server is fine'
fi
