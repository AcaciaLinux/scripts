# scripts
This is a collection of scripts that help manage [AcaciaLinux](https://github.com/AcaciaLinux) resources.

You may clone this repository using the following command:
```bash
git clone --recursive https://github.com/AcaciaLinux/scripts
```
The `--recursive` is needed because this repository uses some convenient parts of [branch](https://github.com/AcaciaLinux/branch), so this addition is needed to make git clone [branch](https://github.com/AcaciaLinux/branch) into this repository too.

## check_file_conflicts.py
This is a very handy script especially for packagers, it takes two arguments: `<source directory>` and `<cache directory>`. `<source directory>` is the directory where the script should look for packages. It scans the directory recursively for `.lpkg` files and extracts them into `<cache directory>` which can be seen as the working directory. In the next step it will index the packages and look for file conflicts that can abort the installation by leaf. It then creates the file `results.txt` that contains a nice overview over the packages with conflicting files.
