import os
from struct import pack

#Returns the full package archive name
def getFullName(package_archive):
	split = package_archive.split('/')
	return str(os.path.splitext(split[len(split)-1])[0])

#Gets the package archive name
def getVersion(package_archive):
	split = getFullName(package_archive).split('-')
	return str(split[len(split)-1])

#Gets the package archive name
def getName(package_archive):
	return str(getFullName(package_archive)).replace("-" + getVersion(package_archive), "")

#Gets the file extension
def getExtension(package_archive):
	split = package_archive.split('.')
	return str(split[len(split)-1])
