#!/usr/bin/python3
import sys
import branch.src.lfpkg as lfpkg

from tools.find_in import *
from tools.extract_packages import *
from tools.leafPackage.leafPackage import LeafPackage

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
    packages.append(LeafPackage(cacheDir + "/" + pkg_name, lfpkg.parse(cacheDir + "/" + pkg_name + "/leaf.pkg")))

for package in packages:
    package.index()

total_conflicts = 0

file_report = open("report.txt", "w")

for src_package in packages:
    print("Checking for file conflicts with", src_package._name)

    for check_package in packages:
        if (src_package != check_package):

            conflicts = src_package.checkConflicts(check_package)

            if (len(conflicts) > 0):
                print("Found {} conflicts between {} and {}".format(len(conflicts), src_package._name, check_package._name))

                total_conflicts += len(conflicts)

                file_report.write("\n{} <=> {} ==> {} conflicts:\n".format(src_package._name, check_package._name, len(conflicts)))

                for file in conflicts:
                    file_report.write("\t{}\n".format(file))

file_report.close()


