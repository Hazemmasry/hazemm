class myclass ():
     def method(self):
       print("1")
     def method2(self,someString):
       print("2")
def main():
   c=myclass()
   c.method()
   c.method2("3")
   d=anotherclass()
   d.method()
   d.method2()


class anotherclass(myclass):

    def method (self):
        print("4")
    def method2 (self):
        myclass.method(self)
        anotherclass.method(self)

        print("3")
    def method3 (self):
        anotherclass.method2(self)



if __name__ == '__main__':
    main()
