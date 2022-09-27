#!python3

from bs4 import BeautifulSoup
import requests
import sys

if (len(sys.argv) != 2):
    print("Usage: {} <package>".format(sys.argv[0]))
    exit(1)

url="https://archlinux.org/packages/core/x86_64/{}".format(sys.argv[1])
deps = []
makedeps = []
req = requests.get(url)
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
                    
depsString = ""
makedepsString = ""

for dep in deps:
    depsString += "[" + dep + "]"

for dep in makedeps:
    makedepsString += "[" + dep + "]"

print("dependencies={}".format(depsString))
print("builddeps={}".format(makedepsString))   
