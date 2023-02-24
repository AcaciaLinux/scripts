import requests
import blog
from bs4 import BeautifulSoup
import packagebuild
import re
import sys

def main():
    if(len(sys.argv) != 2):
        print("USAGE: python3 parse-lfs.py URL")
        return


    blog.info("Sending web request..")
    res = requests.get(sys.argv[1])
    soup = BeautifulSoup(res.content, "html.parser")

    pkg_info = soup.find_all("h1", class_="sect1")[0].contents[2].strip()
    
    res = pkg_info.split("-")
    blog.info("Finding name and version")

    pkg_name = res[0]
    pkg_vers = res[1]

    description_title = soup.find_all("h2", class_="sect2")[0]
    description = description_title.find_next("p").text.replace('\n', '').replace('\t', '').strip()
    description_text = re.sub('\s+', ' ', description).strip()

    blog.info("Parsing package: {}, version: {}".format(pkg_name, pkg_vers))

    blog.info("Finding source link..")
    dl_link = soup.find_all(class_="ulink")[0].get("href")
    blog.info("Source is: {}".format(dl_link))

    blog.info("Finding dependencies..")

    required_deps = [ ]
    
    required_deps_tag = soup.find("p", class_="required")
    for a in required_deps_tag.find_all("a"):
        required_deps.append(a.contents[0].split("-")[0].lower())

    optional_deps = [ ]

    optional_deps_tag = soup.find("p", class_="optional")
    for a in optional_deps_tag.find_all("a"):
        optional_deps.append(a.contents[0].split("-")[0].lower())

    blog.info("Required dependencies: {}".format(required_deps))
    blog.info("Optional dependencies: {}".format(optional_deps))

    
    blog.info("Getting commands..")
    
    cmd_sections = soup.find_all("kbd", class_="command")

    build_section = ""

    for cmd_section in cmd_sections:
        build_section = "{}#NEW SECTION\n{}\n\n".format(build_section, cmd_section.contents[0])


    build_section_arr = build_section.split("\n")
    pkg_build_script = [ ]

    for line in build_section_arr:
        pkg_build_script.append("\t{}".format(line))
    
    blog.info("Creating pkgbuild object..")

    pkg_build = packagebuild.package_build()
    
    pkg_build.name = pkg_name
    pkg_build.version = pkg_vers
    pkg_build.source = dl_link
    pkg_build.description = description_text
    pkg_build.real_version = 0
    pkg_build.dependencies.extend(optional_deps)
    pkg_build.dependencies.extend(required_deps)
    
    pkg_build.build_script = pkg_build_script
    
    
    blog.info("Package build file written..")
    pkg_build.write_build_file("{}.bpb".format(pkg_name))


if(__name__ == "__main__"):
    main()
