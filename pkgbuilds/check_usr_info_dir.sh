#!/bin/sh

#Check for the required argument
if [ $# -eq 0 ]
then
	echo "This script needs the .bpb file to to check for removal of /usr/share/info/dir or the directory containing a package.bpb file"
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

	if ! [ -f $FILE ]
	then
		echo "$FILE does not exist!"
		exit -1
	fi
fi

OUTPUT=$(grep "rm" $FILE | grep "/usr/share/info/dir")
RES=$?

if [ $RES -eq 1 ]
then
	echo "$FILE does not remove /usr/share/info/dir!"
	exit 1
else
	exit $RES
fi

exit 0
