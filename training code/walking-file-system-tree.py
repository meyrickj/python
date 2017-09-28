!#/usr/bin/python3

import os

for dirpath, dirnames, filenames in os.walk("DIR_Here")

    print("files in %s are:" % dirpath)
    for files in filenames:
        print("\t" + file)

    print("Directories in %s are:" % dirpath)
    for dir in dirnames
        pring("\t" + dir)
