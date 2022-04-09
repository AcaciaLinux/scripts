#!/usr/bin/python3
import sys

from tools.find_in import *
from tools.extract_packages import *

if (len(sys.argv) != 2):
    print("This script needs an argument: Package directory")
    exit(-1)

srcDir = str(sys.argv[1])
cacheDir = srcDir + "/cache/"

tar_packages = find_in(srcDir, "lfpkg")

extract_packages(tar_packages, cacheDir)
