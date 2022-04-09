from asyncio import futures
from genericpath import isdir
from socket import getnameinfo
from tokenize import Funny
from unittest.mock import patch
from .pkg_archive.name import *
import os

#Checks the supplied archive in the supplied destination
def check_package_archive(package_archive, destination):
	fullName = getFullName(package_archive)
	name = getName(package_archive)
	version = getVersion(package_archive)

	pkgPath = destination + "/" + fullName + "/"
	
	#First check if the target directory exists
	if (not os.path.isdir(pkgPath)):
		print("Extracted package", fullName, "does not exist")
		return False

	#Check if the leaf.pkg file exists
	if (not os.path.isfile(pkgPath + "leaf.pkg")):
		print("leaf.pkg file of package", fullName, "does not exist")
		return False

	#Check if the data directory exists
	if (not os.path.isdir(pkgPath + "data/")):
		print("Data directory of package", fullName, "does not exist")
		return False	

	return True
