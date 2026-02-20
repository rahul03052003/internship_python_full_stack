#tuple is unchangable
#ordered
#allows duplicates also

tu=("hello",10,True,"hello",50)
#print(tu)
#print(len(tu))

#one value tuple(,)
t2=("apple",)
#print(t2)
#print(type(t2))

#accessing tuple
'''print(tu[0])
print(tu[-3])
print(tu[2:5])'''



'''print("hello" in tu)
if 100 in tu:
    print("Yes it is in tuple")
'''

#update tuple(tuple to list)
'''x=("Apple","Mango","Strawberry")
y=list(x)
print(type(y))

y[0]="Orange"
y.insert(1,"Grapes")#we can use append also
z=tuple(y)

print(z)
print(type(z))
'''

#removing items from tuple by converting datastructure
'''x=list(tu)
print(x.pop(1))
print(x)
z=tuple(x)
print(z)
'''

#deleting
'''del tu
print(tu)'''

#unpacking tuple
'''cars=("Benz","Defender","Audi","BYD")
(rr,df,au,bd)=cars
print(rr)'''

#joining the tuples
'''tu2=("Benz","Defender","Audi","BYD")
tu3=tu+tu2
print(tu3)
'''

#multiplying tuple values
'''tu4=("Benz","Defender","Audi","BYD")*2
print(tu4)
'''


