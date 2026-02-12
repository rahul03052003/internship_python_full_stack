#inheritance single,super(),multilevel

class A:
    def add(self,a,b):
        c=a+b
        print("Addition result is: ",c)
    def sub(self,a,b):
        c=a-b
        print("Subtraction result is: ",c)
    def display(self):
        print("Inside display")
        
class B:
    def div(self,a,b):
        ''''a1=A()
        a1.add(10,20)'''
        a1=A()
        a1.add(a,b)
        c=a/b
        print("Addition result is: ",c)
    def display(self):
        print("Inside display")
        
class C(A):
    #overriding
    def add(self,a,b):
        #super().add(a,b)
        tax=20
        c=a+b+tax
        print("Addition result is: ",c)
    def welcomeMessage(self):
        print("Welcome to the software")
    
#b1=B()
#b1.div(10,20)

a1=A()
a1.add(10,20)
'''
a1.sub(10,2)
a1.display()
'''


'''c1=C()
c1.add(30,40)
c1.welcomeMessage()
'''


#multi-level
class D(C):
    #overriding method
    def add(self,a,b):
        super().add(10,20)
        gst=10
        ses=5
        c=a+b+gst+ses
        print("Addition result with gst & ses :",c)
    def m1():
        print("Inside m1")

d1=D()
d1.add(10,20)
d1.welcomeMessage()
d1.display()
