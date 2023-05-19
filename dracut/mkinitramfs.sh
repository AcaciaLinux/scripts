#!/bin/sh

set +e

if [ -z $1 ]; then
	SEARCHDIR="/boot"
else
	SEARCHDIR="$1"
fi

find "$SEARCHDIR" -name "*linu*" |  while read KERNEL_FILE; do

	file "$KERNEL_FILE" | grep "Linux kernel" > /dev/null
	if [ $? -eq "1" ]; then
		continue
	fi

	echo "$KERNEL_FILE is a kernel, building initramfs..."
	KERNEL_FULL_NAME=$(basename "$KERNEL_FILE")
	KERNEL_NAME=$(echo "$KERNEL_FULL_NAME" | cut -d '-' -f1)
	KERNEL_APPENDIX=$(echo "$KERNEL_FULL_NAME" | sed "s/$KERNEL_NAME//g")
	KERNEL_VERSION=$(file -bL $KERNEL_FILE | sed -n '/version /!q1;s/.*version //;s/ .*//p')

	INITRAMFS_FILE="initramfs$KERNEL_APPENDIX.img"

	echo "Kernel name: $KERNEL_NAME"
	echo "Kernel version: $KERNEL_VERSION"
	echo "Generating initramfs file: $INITRAMFS_FILE, this might take some time..."

	LOG=$(dracut --kver "$KERNEL_VERSION" --force "$SEARCHDIR/$INITRAMFS_FILE" 2>&1)
	echo "$LOG" > $SEARCHDIR/$INITRAMFS_FILE.build.log
done

