import os
import sys

# Upgrade Branch Package Build files:
# Add missing fields to older package builds
# Usage: bpb_upgrade.py $FILE

class BPBOpts():
    def __init__(self):
        self.name = ""
        self.version = ""
        self.real_version = ""
        self.dependencies = ""
        self.description = ""
        self.build_dependencies = ""
        self.build_script = [ ]

def parse_build_file(pkg_file):
    build_file = open(pkg_file, "r")
    build_arr = build_file.read().split("\n")

    BPBopts = BPBOpts()

    BPBopts.name = ""
    BPBopts.version = ""

    # set to 0 if we dont have any
    BPBopts.real_version = 0


    BPBopts.source = ""
    BPBopts.dependencies = ""
    BPBopts.description =  ""
    BPBopts.build_dependencies = ""

    build_opts = False
    command = ""
    for prop in build_arr:
        if(build_opts):
            if(prop == "}"):
                build_opts = False
                continue

            # remove tab indentation
            prop = prop.replace("\t", "")

            # skip empty lines
            if(len(prop) == 0):
                continue;

            BPBopts.build_script.append(prop)
        else:
            prop_arr = prop.split("=")
            key = prop_arr[0]

            if(len(key) == 0):
                continue

            if(len(prop_arr) != 2):
                print("Broken package build file. Failed property of key: ", key)
                return -1

            val = prop_arr[1]

            if(key == "name"):
                BPBopts.name = val
            elif(key == "version"):
                BPBopts.version = val
            elif(key == "real_version"):
                BPBopts.real_version = val
            elif(key == "source"):
                BPBopts.source = val
            elif(key == "dependencies"):
                BPBopts.dependencies = val
            elif(key == "description"):
                BPBopts.description = val
            elif(key == "builddeps"):
                BPBopts.build_dependencies = val
            elif(key == "build"):
                build_opts = True

    return BPBopts

def write_build_file(file, pkg_opts):
    bpb_file = open(file, "w")
    bpb_file.write("name={}\n".format(pkg_opts.name))
    bpb_file.write("version={}\n".format(pkg_opts.version))
    bpb_file.write("real_version={}\n".format(pkg_opts.real_version))
    bpb_file.write("source={}\n".format(pkg_opts.source))
    bpb_file.write("dependencies={}\n".format(pkg_opts.dependencies))
    bpb_file.write("builddeps={}\n".format(pkg_opts.build_dependencies))
    bpb_file.write("description={}\n".format(pkg_opts.description))
    bpb_file.write("build={\n")
    
    print("Uniform indentation for build={}...")

    for line in pkg_opts.build_script:
        bpb_file.write("\t")
        bpb_file.write(line)
        bpb_file.write("\n")

    bpb_file.write("}")
    print("package.bpb file written!")

def main():
    if(len(sys.argv) != 2):
        print("Usage: bpb_upgrade.py <FILE>")
        return -1

    file = sys.argv[1]

    if(not os.path.exists(file)):
        print("File not found.")
        return -1

    print("Parsing file {}...".format(file))
    pkg_build = parse_build_file(file)

    if(pkg_build == -1):
        print("Parsing failed.")
        return -1

    print("=================================")
    print("Package information:")
    print("name: ", pkg_build.name)
    print("version: ", pkg_build.version)
    print("real_version: ", pkg_build.real_version)
    print("source: ", pkg_build.source)
    print("dependencies: ", pkg_build.dependencies)
    print("description: ", pkg_build.description)
    print("build_dependencies: ", pkg_build.build_dependencies)
    print("build_script: ")
    for line in pkg_build.build_script:
        print(line)
    print("=================================")
    
    print("Writing to disk...")
    write_build_file(file, pkg_build)

    print("=================================")
    print("Package information:")
    print("name: ", pkg_build.name)
    print("version: ", pkg_build.version)
    print("real_version: ", pkg_build.real_version)
    print("source: ", pkg_build.source)
    print("dependencies: ", pkg_build.dependencies)
    print("description: ", pkg_build.description)
    print("build_dependencies: ", pkg_build.build_dependencies)
    print("build_script: ")
    for line in pkg_build.build_script:
        print(line)
    print("=================================")
    print("Done!")

if(__name__ == "__main__"):
    main()








