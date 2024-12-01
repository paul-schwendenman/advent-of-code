#! /usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "illegal number of parameters"
    exit 1
fi

if [ ! -f day$1.py ]; then
    cp dayXX.py day$1.py
    touch day$1.in day$1.example
    code day$1.py day$1.in day$1.example
elif [ ! -f test_day$1.py ]; then
    cp test_dayXX.py test_day$1.py
    code test_day$1.py
else
    code day$1.py day$1.in day$1.example
fi
