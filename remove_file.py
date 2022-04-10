#!/usr/bin/python3

#This script goes through every .lfpkg file in a specified directory, extracts it, removes the specified files and repackages it
import sys
import os

from tools.find_in import *
from tools.extract import extract
from tools.leafPackage.leafPackage import LeafPackage
import branch.src.lfpkg as lfpkg

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

#Extract the packages
print("Extracting:")
for path in packages_paths:
	print("=> {}".format(path))

	#Create the extracting directory path
	extractSplit = str(path).split('/')
	extractDir = str(path).replace(extractSplit[len(extractSplit)-1], "")

	#Extract the package
	extract(srcDir + path, cacheDir + "/" + extractDir)


packages = []
lfpkg_files = find_in(cacheDir, "leaf.pkg")

#Index the packages
print("Parsing:")
for lfpkg_file in lfpkg_files:
	print("=> {}".format(lfpkg_file))

	split = lfpkg_file.split('/')
	pkgRoot = lfpkg_file.replace(split[len(split)-1], "")

	packages.append(LeafPackage(pkgRoot, lfpkg.parse(lfpkg_file)))

print("Checking:")
for package in packages:
	print("=> {}".format(package.getFullName()))

	checkPath = package._pkgRoot + "/data/" + file_remove
	
	if (os.path.exists(checkPath)):
		if (not os.path.isdir(checkPath)):
			os.remove(checkPath)
			print("\tFound and removed {}".format(file_remove))

print("Repackaging:")
for package in packages:
	print("=> {}".format(package.getFullName()))

	#Create the extracting directory path
	tarDir = str(package._pkgRoot).replace(package.getFullName(), "")

	package.tar(tarDir + "/" + package.getFullName() + ".lfpkg")