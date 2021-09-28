def main():

    x = open("fe.txt","r")
    return x


x = main()
#for i in range(100):
    #e=input("what is your name")
 #   x.write("hi"+str(i)+"\r\n")
if x.mode=="r":
    contents= x.read()
    print(contents)
x.close()
