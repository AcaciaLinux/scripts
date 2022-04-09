#!/usr/bin/python3
import sys
import branch.src.lfpkg as lfpkg

from tools.find_in import *
from tools.extract_packages import *
from tools.leafPackage.leafPackage import LeafPackage

if (len(sys.argv) != 3):
    print("This script needs two arguments: <source directory> <cache directory>")
    exit(-1)

srcDir = str(sys.argv[1])
cacheDir = str(sys.argv[2])

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

packages_with_conflicts = []

for src_package in packages:
    print("Checking for file conflicts with", src_package._name)

    for check_package in packages:
        if (src_package._name != check_package._name):

            conflicts = src_package.checkConflicts(check_package)

            if (len(conflicts) > 0):
                print("Found {} conflicts between {} and {}".format(len(conflicts), src_package._name, check_package._name))

                total_conflicts += len(conflicts)
                packages_with_conflicts.append(src_package)

                file_report.write("\n{} <=> {} ==> {} conflicts:\n".format(src_package._name, check_package._name, len(conflicts)))

                for file in conflicts:
                    file_report.write("\t{}\n".format(file))

file_report.write("=> Packages with conflicts:\n")

for package in packages_with_conflicts:
    file_report.write("\t==> {}\n".format(package._name))

file_report.write("\nTotal conflicts: {}\n".format(total_conflicts))

file_report.close()

print("Total conflicts found: {}\n".format(total_conflicts))
