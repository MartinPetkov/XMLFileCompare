#!/bin/sh

# Small script to run the Python function and compare the two files

mkdir -p "tmp"

file1="books.xml"
file2="books_bad_order.xml"

# Put the files into canonical form
xmllint --c14n $file1 > ./tmp/$file1
xmllint --c14n $file2 > ./tmp/$file2

for n in $(seq 1 20); do
  # Compare results
  echo "Round $n:"
  python compare_xml.py ./tmp/$file1 ./tmp/$file2
done

rm -rf ./tmp
