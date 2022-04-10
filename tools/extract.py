import tarfile
from .check_package_archive import check_package_archive

def extract(path: str, destination: str):
	print("Extracting {} into {}...".format(path, destination))

	#Try opening the package
	try:
		pkg = tarfile.open(path)
	except:
		print("Failed to open package archive", path)
		pkg.close()
		return False
	
	#Try extracting the package
	try:
		pkg.extractall(path=destination)
		pkg.close()
	except:
		print("Failed to extract package", path)
		pkg.close()
		return False

	#Check its contents
	if (check_package_archive(path, destination) != True):
		print("Checks for package", path, "failed!")
		return False

	return True
