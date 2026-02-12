#methods
def display():
    print("This is display method")
    
def addition(a,b):
    print("Inside addition method")
    sum=a+b
    print("Addition sum is: ",sum)

def multiply(a,b):
    print("Inside multiply method")
    mul=a*b
    print("Multiplication result is: ",mul)
    return mul

def displayDetails(name,age,college="VTU"):
    print("Name is : ",name)
    print("Age is :",age)
    print("College is :",college)

    
#display

#display()
#addition(2,3)
#z=multiply(10,5)
print("Data from z: ",z)
displayDetails("Ravi",26,"Mysore University")
