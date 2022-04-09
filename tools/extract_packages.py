import tarfile
import os
from traceback import print_stack
from .check_package_archive import *
from .pkg_archive.name import *

def extract_packages(src_pkgs, destination):

	#Check the destination directory
	if (os.path.isdir(destination)):
		print("Using existing destination", destination)
	else:
		print("Creating destination", destination + "...")

	packages = []

	#Walk through every package package archive
	for src_pkg in src_pkgs:
		print("Extracting", src_pkg + "...")

		#Try opening the package
		try:
			pkg = tarfile.open(src_pkg)
		except:
			print("Failed to open package archive", src_pkg)
			print_stack()
			pkg.close()
			continue
		
		#Try extracting the package
		try:
			pkg.extractall(path=destination)
			pkg.close()
		except:
			print("Failed to extract package", src_pkg)
			print_stack()
			pkg.close()
			continue

		#Check its contents
		if (check_package_archive(src_pkg, destination) != True):
			print("Checks for package", src_pkg, "failed!")
			continue
		
		packages.append(getFullName(src_pkg))

	return packages