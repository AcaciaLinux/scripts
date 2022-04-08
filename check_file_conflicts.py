#!/usr/bin/python3
import sys
import os
import tarfile

from os import listdir

if (len(sys.argv) != 2):
    print("This script needs an argument: Package directory")
    exit(-1)

srcDir = str(sys.argv[1])
cacheDir = srcDir + "/cache/"

if (os.path.isdir(cacheDir)):
    print("Using existing cache directory", cacheDir)
else:
    print("Creating cache directory", cacheDir)
    os.mkdir(cacheDir)

packages = []

for root, dirs, files in os.walk(srcDir):
    for file in files:
        #Split the filename to get the file extension
        split = file.split('.')
        fType = split[len(split)-1]

        #If the extension indicates a leaf package, add it
        if (fType == "lfpkg"):
            packages.append(os.path.join(root, file))

for name in packages:
    print("Found package: " + name)

for path in packages:
    print("Extracting", path + "...")

    pkg = tarfile.open(path)
    try:
        pkg.extractall(path=cacheDir)
    except:
        print("Failed to extract", path)

    pkg.close()

