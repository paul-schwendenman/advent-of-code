#! /usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "illegal number of parameters"
fi

if [ ! -f day$1.py ]; then
    cp dayXX.py day$1.py
    touch day$1.in day$1.example
elif [ ! -f test_day$1.py ]; then
    cp test_dayXX.py test_day$1.py
fi
