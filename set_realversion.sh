#!/bin/sh

#Check for the required argument
if [ $# -ne 2 ]
then
	echo "Usage: $0 <.bpb file / parent dir of package.bpb> <realversion to set>"
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

#Extract package name
PKGNAME=$(cat $FILE | grep "name=" | cut -d'=' -f2)

#Extract real version
CURVER=$(cat $FILE | grep "real_version" | cut -d'=' -f2)
#Set the new version
NEWVER=$2

#Inform the user
echo "Current real_version of package $PKGNAME: $CURVER, new real_version: $NEWVER"

#Replace the version in the file
sed -i "s/real_version\=$CURVER/real_version\=$NEWVER/" $FILE
