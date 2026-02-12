#control statements
#direct boolean value
'''condition=bool(input("Value: "))
if condition==True:
    print("inside if")'''
    
#if else
'''age=input("Enter value: ")
if int(age)>=18:
    print("You can vote")
else:
    print("You can nt vote")
print("Outside if")'''

#if elif else
'''marks=int(input("Enter marks:"))
if marks<35:
    print("Student Failed")
elif marks==35:
    print("Just pass")
elif marks>35 and marks<60:
    print("Second class")
elif marks>=60 and marks<75:
    print("First class")
elif marks>=75 and marks<=100:
    print("Distinction")
else:
    print("Incorrect marks entered")'''


#nest if elif else
#one if or elif or else having if elif else inside called as an nested if
'''a=int(input("Enter the value: "))
if a>10:
    print("A is greater than 10")
    if a==15:
        print("A is == 15")
    elif a==20:
        print("A is == 20")
    else:
        print("Inside nested else")
elif a<10:
    print("A is less than 10")
    if a==5:
        print("A is == 5")
    else:
        print("inside elif nested else")
else:
    print("Invalid")'''

#short hand if
'''a=1
if a==1: print("hello short hand if")'''

#short hand if else
'''a=6
print("Hello") if a==5 else print("Bye")'''

#loops
#while
'''while True:
    print("infinite loop")'''
'''b=True
while b:
    print("Boolean controled while loop")
    b=False
'''

#while loop with break keyword
'''a=0
while a<10:
    print("A is = ",a)
    a+=1
    if a==5:
        break
'''

#while loop with continue
'''a=0
while a<10:
    print("A is = ",a)
    a+=1
    if a==5:
        continue
    print("Hello")

'''

#for loop
'''for x in range(10):
    print(x)
    '''
'''for x in range(1,10):
    print(x)'''
'''for x in range(1,10,2):
    print(x)'''
'''cars=["volvo","benz","audi"]
for i in cars:
    print(i)'''
'''for z in "hello":
    print(z)'''

#pass keyword
age=20
if age>18:
    pass
else:
    print("Inside else")
