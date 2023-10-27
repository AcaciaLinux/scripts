#!python3

from bs4 import BeautifulSoup
import requests
import sys

if (len(sys.argv) < 2):
    print("Usage: {} <package> (optional)<repo>".format(sys.argv[0]))
    exit(1)
    
repo = "core"
if (len(sys.argv) >= 3):
    repo = sys.argv[2]

url="https://archlinux.org/packages/{}/x86_64/{}".format(repo, sys.argv[1])
deps = []
makedeps = []
req = requests.get(url)

if (req.status_code != 200):
    print("Error in fetching data: {}".format(req.status_code))
    exit(1)

soup = BeautifulSoup(req.text, "html.parser")
for div in soup.findAll("div", id="pkgdeps"):
    lis = div.findAll("li")
    for li in lis:
        if (len(li) == 3):
            for entry in li.findAll("a"):
                deps.append(entry.text)
                makedeps.append(entry.text)
     
        else:
            if (len(li.findAll("span", {'class':'make-dep'})) != 0):
                for entry in li.findAll("a"):
                    makedeps.append(entry.text)
                    

# Remove duplicates
deps = list(set(deps))
makedeps = list(set(makedeps))

# remove git, glibc and stuff that is not needed
if "glibc" in makedeps:
    makedeps.remove("glibc")

if "git" in makedeps:
    makedeps.remove("git")

depsString = ""
makedepsString = ""

for dep in deps:
    depsString += "[" + dep + "]"

for dep in makedeps:
    makedepsString += "[" + dep + "]"

print("dependencies={}".format(depsString))
print("builddeps={}".format(makedepsString))   
