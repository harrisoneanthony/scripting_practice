#!/bin/bash

for file in *.HTM; do
	name=$(basename "$file" .HTM)
	# echo mv "$file" "$name.html" #use this line to instead of line 6 to print what the script does before actually modifying the files
	mv "$file" "$name.html"
done
