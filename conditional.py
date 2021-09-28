def main():
    x,y=input("enterx"),input("enter y")
   # if x>y:
       # st="x is greater than y"
    #else:
      #  st="x is less than y"
   # print(st)
    st= "x is greater than y" if (x>y) else "y is greater than x"
    print(st)

if __name__=="__main__" :
    main()