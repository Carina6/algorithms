#!/bin/bash

if [ -n $1 ]; then 
    echo $1
    git checkout $1 

fi 

git pull
