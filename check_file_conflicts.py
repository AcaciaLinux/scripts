#!/usr/bin/python3

import sys
import os
import tarfile

if (len(sys.argv) != 3):
    print("This script needs two arguments: Two .lfpkg files!")
    exit(-1)

file1 = sys.argv[1]
file2 = sys.argv[2]

#Check if the first file is a leaf package
split = file1.split('.')
if (split[len(split)-1] != "lfpkg"):
    print("The first file is not a .lfpkg file!")
    exit(1)

#Check if the second file is a leaf package
split = file2.split('.')
if (split[len(split)-1] != "lfpkg"):
    print("The second file is not a .lfpkg file!")
    exit(1)

print("Checking for file conflicts between", sys.argv[1], "and", sys.argv[2])

os.mkdir("compare")

pkg1 = tarfile.open(file1, 'r')
pkg2 = tarfile.open(file2, 'r')
