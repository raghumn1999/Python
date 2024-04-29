#!/bin/bash

type_of_instance=$1
if [ $type_of_instance == "t2.micro" ]
then
    echo "we can create $1 instance"
else
    echo "we can't create the $1 instance"
fi
