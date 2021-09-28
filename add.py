def main():
    x=open("filll.txt","w+")
    return x
x=main()
for i in range(10):
    x.write("this is a line"+str(i)+"\r\n")
x.close()