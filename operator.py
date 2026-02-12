#operators
#Arithmetic : +,-,/,*,%,**,//
#Assignment : =,+=,-=,*=,%=
#comparision/relational : ==, >,<,>=,<=, !=
#logical : and , or , not
#identity : is, is not
#Membership  : in, not in


#Arithmetic 
a = 10
b = 20
c = a+b
print("addition result is ",c)
c = a-b
print("sub result is ",c)

#exponential
a = 2
b = 3
c = a**b # 2*2*2
print("the result is ",c)

#floor division
a = 2
b = 3
c = a//b # 
print("the result is ",c)
#continue other operators in this

#Assignment
a = 5
b = 10
a +=b
print("result is ", a)

#comparision / Relational operators
a = 6
b = 5
c = a!=b
print(">= result is ",c)


#logical
#and
d = 5
c = a>b and a>d
print("and op result is ",c)

#or
c = a>b or a==d
print("or op result is ",c)
#not
e = not c
print("not op result is ", e)

#identity
a = 10
b = 10
print("==", a==b)
print("identity is op ", a is b)

indian_cars = ["volvo" , "benz", "audi"]
us_cars = ["volvo" , "benz", "audi"]

print("car == ", indian_cars==us_cars)
print("car is op ", indian_cars is not us_cars)

#membership
x = "hello how are you"
y = "h"
print("in op result ", y not in x)

















