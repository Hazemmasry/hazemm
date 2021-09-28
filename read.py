def main():
    x=open("filll.txt","r")
    return x
x=main()
if x.mode=="r":
    contents=x.read()
    print(contents)
x.close()
