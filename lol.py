import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # print(os.name)
    # print("item exist : " + str(path.exists("fefe.txt")))
    # print("item is pdf: " + str(path.islink("fy.x")))
    # print("item is file: " + str(path.isfile("fe.txt")))
    # print(" real path : " + str(path.realpath("fe.txt")))
    # print("item path and name : " + str(path.split(path.realpath("fe.txt"))))
    # t = time.ctime(path.getatime("fe.txt"))
    # print(datetime.datetime.fromtimestamp(path.getatime("fe.txt")))
    # td = datetime.datetime.now()-datetime.datetime
    # print(t)
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("fe.txt"))
    print("it has been : " + str(td) + "since it has been created")
    sec = td.total_seconds()
    d=sec/(3600*60)
    print(str(d))


if __name__ == '__main__':
    main()
