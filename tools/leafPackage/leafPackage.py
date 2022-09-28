import tarfile
from .lfpkg import *
from ..find_in import find_in_ext

class LeafPackage():
	#_files = []

	#_pkgRoot: str
	#_name: str
	#_version: int
	#_description: str
	#_dependencies = []

	def __init__(self, pkgRoot, lfpkg_file: lfpkg):
		self._pkgRoot = pkgRoot

		self._name = lfpkg_file.name
		self._version = lfpkg_file.version
		self._description = lfpkg_file.description
		self._dependencies = lfpkg_file.dependencies
		self._files = []

	def getFullName(self):
		return str(self._name + "-" + self._version)

	def index(self):

		foundFiles = find_in_ext(self._pkgRoot + "/data")

		for file in foundFiles:
			self._files.append(file.replace(self._pkgRoot + "/data", ""))
	

		print("Found", len(self._files), "files in", self._pkgRoot)

		pass

	def checkConflicts(self, otherPkg):
		return list(set(self._files) & set(otherPkg._files))

	def tar(self, targetFile: str):
		print("Taring {} to {}...".format(self.getFullName(), targetFile))

		tar_file = tarfile.open(targetFile, "w:xz")

		for root, dirs, files in os.walk(self._pkgRoot):
			for file in files:
				print("Adding to tarfile: {}".format(os.path.join(root, file)))
				tar_file.add(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self._pkgRoot, '..')))

		tar_file.close()
