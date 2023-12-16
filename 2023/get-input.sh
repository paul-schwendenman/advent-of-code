#! /usr/bin/env bash

YEAR=2023

if [ $# -ne 1 ]; then
    echo "illegal number of parameters"
    exit 1
fi

if [[ ! -v AOC_SESSION ]]; then
    echo "AOC_SESSION is not set"
    exit 2
fi

if [ ! -f day$1.in ] || [ ! -s day$1.in ]; then
    curl https://adventofcode.com/$YEAR/day/$1/input --cookie "session=$AOC_SESSION" -o day$1.in
fi
