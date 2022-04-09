import tarfile
import os
from traceback import print_stack

def extract_packages(src_pkgs, destination):

	#Check the destination directory
	if (os.path.isdir(destination)):
		print("Using existing destination", destination)
	else:
		print("Creating destination", destination + "...")

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
