#
# script to add hash to old meta files
#

import sys
import json
import os
import packagebuild

def main():
    if(not os.path.exists("branch.meta")):
        print("No meta file found!")
        return

    file = open("branch.meta", "r")
    meta = json.loads(file.read())
    file.close()
   
    for vd in meta["version_dependencies"]:
        if(type(meta["version_dependencies"][vd]) is str):

            dep_str = meta["version_dependencies"][vd]
            print("version_dependency is a string, upgrading..: {}".format(dep_str))
            
            res = packagebuild.package_build.parse_str_to_array(dep_str)
            
            meta["version_dependencies"][vd] = res

        else:
            print("Already up to date: {}".format(vd))
    
    print("Writing to disk..")
    jm = json.dumps(meta, indent=4)
    file = open("branch.meta", "w")
    file.write(jm)

if(__name__ == "__main__"):
    main()
