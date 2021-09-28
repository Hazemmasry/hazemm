def main():
    x=open("filll.txt","r")
    return x
x=main()
if x.mode=="r":
    fl=x.readline()
    for x in fl:
        print(x)