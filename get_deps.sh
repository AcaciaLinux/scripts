#!/bin/sh

#Check for the required argument
if [ $# -eq 0 ]
then
	echo "This script needs the .bpb file to increment the realversion of or the directory containing a package.bpb file"
	exit -1
fi

if [ -d $1 ]
then
	FILE=$1/package.bpb
	if ! [ -f $FILE ]
	then
		echo "$FILE does not exist!"
		exit -1
	fi
else
	FILE=$1
fi

echo $(cat $FILE | grep "dependencies=")
echo $(cat $FILE | grep "builddeps=")
echo $(cat $FILE | grep "crossdeps=")
