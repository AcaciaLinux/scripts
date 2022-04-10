
from branch.src.lfpkg import *
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

	def index(self):

		foundFiles = find_in_ext(self._pkgRoot + "/data")

		for file in foundFiles:
			self._files.append(file.replace(self._pkgRoot + "/data", ""))
	

		print("Found", len(self._files), "files in", self._pkgRoot)

		pass

	def checkConflicts(self, otherPkg):
		return list(set(self._files) & set(otherPkg._files))
