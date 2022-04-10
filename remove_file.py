#!/usr/bin/python3

#This script goes through every .lfpkg file in a specified directory, extracts it, removes the specified files and repackages it
import sys
import os

from tools.find_in import *
from tools.extract import extract

if (len(sys.argv) < 3):
	print("Please specify at least the path to search and one file to remove!")
	exit(1)

cacheDir = ".cache/"

if (not os.path.isdir(cacheDir)):
	print("Creating cache dir {}...".format(cacheDir))
	os.mkdir(cacheDir)

srcDir = sys.argv[1]
file_remove = sys.argv[2]
packages_paths = find_in_ext_relative(srcDir, "lfpkg")
relative_dirs = []

#Extract the packages
print("Extracting:")
for path in packages_paths:
	print("=> {}".format(path))

	#Create the extracting directory path
	extractSplit = str(path).split('/')
	extractDir = str(path).replace(extractSplit[len(extractSplit)-1], "")

	#Extract the package
	extract(srcDir + path, cacheDir + "/" + extractDir)

#for path in packages_paths:
#	cache = str(path).replace(srcDir, "")
#	#Don't look at this, just some magic....
#	cache = cache.replace(cache.split('/')[len(cache.split('/'))-1], "")
#	relative_dirs.append(cache)
#	print("Relative path of {}: {}".format(path, cache))

#print("Found packages:")
#for path in packages_paths:
#	print("=> {}".format(path))
#	extract(path, cacheDir + "/" + relative_dirs[packages_paths.index(path)])

#for path in relative_dirs:
#	checkPath = cacheDir + "/" + path + "/data/" + file_remove
#	print("Checking if {} exists...".format(checkPath))
#	
#	if (os.path.exists(checkPath)):
#		print("File " + file_remove + " exists!")
