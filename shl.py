import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    if path.exists("file.txt"):
        scr = path.realpath("file.txte")
        des = scr + ".bak"
        # shutil.copy(scr,des)
        # shutil.copystat(scr,des)
        # os.rename("file.txt", "hazemmm.txt")
        # root_dir, tail=path.split(scr)
        # shutil.make_archive("archieve","zip",root_dir)
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == '__main__':
    main()
