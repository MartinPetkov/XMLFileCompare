#!/bin/sh

# Small script to run the Python function and compare the two files

mkdir -p "tmp"

# Put both files into canonical form
xmllint --c14n $1 > ./tmp/$1
xmllint --c14n $2 > ./tmp/$2

# Compare results
python compare_xml.py ./tmp/$1 ./tmp/$2

rm -rf ./tmp
