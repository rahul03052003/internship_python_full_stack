#multiple inheritance

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def m1(self):
        print("Inside class A m1 method")
    def m2(self):
        print("Inside class A m2 method")

class B:
    def m3(self):
        print("Inside class B m3 method")
    def m4(self):
        print("Inside class B m4 method")

class C(A,B):
    def __init__(self,name,age):
        super().__init__(name,age)
    def m5(self):
        print("Inside class C m5 method")

c1=C("Python",60)
c1.m5()
c1.m1()
c1.m3()
print(c1.name)
print(c1.age)
