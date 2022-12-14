#!/bin/sh

set +e

#Check for the required argument
if [ $# -ne 2 ]
then
	echo "Usage: $0 <.lfpkg file> <cache directory>"
	exit -1
fi

LFPKG=$(realpath $1)
CACHE=$(realpath $2)

EXT="${LFPKG##*.}"

if [[ "$EXT" != "lfpkg" ]]
then
	echo "The file has to be a .lfpkg file"
	exit -2
fi

PKGNAME=$(sed s/.lfpkg// <<< $(basename $LFPKG))

OLDWD=$(pwd)

mkdir -pv $CACHE
cd $CACHE

echo "Extracting $PKGNAME..."
tar xpf $LFPKG

cd $CACHE/$PKGNAME/data

while read -r line;
do
	(strip --strip-unneeded $line 2>&1) > /dev/null
	if [ $? -eq 0 ]
	then
		echo "Stripped $line"
	fi
done <<< $(find . -type f)

cd $CACHE
echo "Recompressing $PKGNAME..."
tar cJpf $OLDWD/$PKGNAME.lfpkg $CACHE/$PKGNAME
