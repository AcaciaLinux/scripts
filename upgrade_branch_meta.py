#
# script to add hash to old meta files
#

import sys
import json
import os
import hashlib

def main():
    if(not os.path.exists("branch.meta")):
        print("No meta file found!")
        return

    file = open("branch.meta", "r")
    meta = json.loads(file.read())
    file.close()
    
    if("version_hashes" in meta):
        print("Already has version hashes..")
        return

    meta["version_hashes"] = { }

    for vr in meta["versions"]:
        if(os.path.exists(vr)):
            pkg_name = os.listdir(vr)[0]
            print("Adding hash for {} vers {}".format(pkg_name, vr))
            
            pkg_path = os.path.join(vr, pkg_name)

            md5_hash = hashlib.md5()
            hash_file = open(pkg_path, "rb")

            for chunk in iter(lambda: hash_file.read(4096), b""):
                md5_hash.update(chunk)

            h = md5_hash.hexdigest()
            print("Hash: " + h)
            
            meta["version_hashes"][vr] = h
    
    print("Writing to disk..")
    jm = json.dumps(meta, indent=4)
    file = open("branch.meta", "w")
    file.write(jm)

if(__name__ == "__main__"):
    main()
