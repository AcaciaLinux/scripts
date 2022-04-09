#!/usr/bin/python3
import sys
import branch.src.lfpkg as lfpkg

from tools.find_in import *
from tools.extract_packages import *

if (len(sys.argv) != 2):
    print("This script needs an argument: Package directory")
    exit(-1)

srcDir = str(sys.argv[1])
cacheDir = srcDir + "/cache/"

tar_packages = find_in(srcDir, "lfpkg")

package_names = extract_packages(tar_packages, cacheDir)

packages = []

for pkg_name in package_names:
    print("Parsing package", pkg_name + "...")
    newPack = lfpkg.parse(cacheDir + "/" + pkg_name + "/leaf.pkg")
    packages.append(newPack)


