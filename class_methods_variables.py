#class,methods,variable

class Arithmetic:
    #class variable
    college="VTU"
    
    def __init__(self,name,age):
        #object variables
        self.name=name
        self.age=age
        
    def accessingObjectV(self):
        print("Inside accessingObjectV")
        print(self.name)

    def accessingClassV(self):
        print("Inside accessingClassV")
        print(Arithmetic.college)
        
    def display(self):
        print("This is display method")
        
    def addition(self,x,y):
        print("Inside addition")
        c=x+y
        print("Addition result is ",c)
        
#creating object
'''a=Arithmetic()
a.display()
a.addition(20,10)

a2=Arithmetic()
a2.display()
a2.addition(50,10)
'''

#creating object with init method
a3=Arithmetic("Arun",25)
print(a3.name)
a3.accessingObjectV()
a3.accessingClassV()
print("Accessing class variable: ",Arithmetic.college)
