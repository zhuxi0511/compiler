#! /bin/sh

if [ $# = 0 ]; then
    echo 'error'
    exit 1
fi

if [ $1 = 's' ]; then
    python syntax_analysis.py $2
    exit
fi

if [ $1 = 'r' ]; then
    python syntax_analysis.py $2
    gcc text.s
    ./a.out
    exit
fi
