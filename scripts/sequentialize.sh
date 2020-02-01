#!/bin/bash
# e.g: ./sequentialize.sh db_images

DIRNAME="$1"
NEWDIR="facedb_renamed"

if [ ! -d "$DIRNAME" ]; then
	echo "Not a valid directory path."
	exit
fi

if [ -z "$DIRNAME" ]; then
	echo "Pass me the directory to sequentialize!"
	exit
fi

if [ ! -d "$NEWDIR" ]; then
	mkdir "$NEWDIR"
fi

n=0
FILES=($(find "$DIRNAME"/*))
for filename in "${FILES[@]}"; do
	cp "$filename" "./$NEWDIR/img$n.jpg"
	n=$((n + 1))
done

