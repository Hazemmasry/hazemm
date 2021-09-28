def main():
    x=open("filll.txt","a")
    return x
x=main()
for i in range(10):
    x.write("call"+str(i)+"\n\r")
x.close()