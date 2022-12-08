#!/bin/sh

#Check for the required argument
if [ $# -eq 0 ]
then
	echo "This script needs the .bpb file to increment the realversion of"
	exit -1
fi

FILE=$1

#Extract package name
PKGNAME=$(cat $FILE | grep "name=" | cut -d'=' -f2)

#Extract real version
CURVER=$(cat $FILE | grep "real_version" | cut -d'=' -f2)
#Increment it
NEWVER=$((CURVER+1))

#Inform the user
echo "Current real_version of package $PKGNAME: $CURVER, new real_version: $NEWVER"

#Replace the version in the file
sed -i "s/real_version\=$CURVER/real_version\=$NEWVER/" $FILE
