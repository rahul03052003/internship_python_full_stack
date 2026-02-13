#List data structure
#mutable datatype(chnages are actually possible)

'''
l1=["Cars","Bus","Truck","Van"]
print(l1)
print(type(l1))

l2=[10,20,30,40]
print(l2)
print(type(l2))

l3=[True,False,True]
print(l3)
print(type(l3))
'''

l4=["volvo",123,True,123.45]
#accessing list
'''
print(l4)
print(l4[1])
#print(type(l4))'''


#searching inside list using in operator

'''if "volvo" in l4:
    print("Yes volvo found")
'''
#changing list values
'''l4[2]="german"
print(l4)'''

'''l4[1:4]=["america","france","italy"]
print(l4)
'''

#inserting inside list
'''print(l4)
l4.insert(2,"Bye")
print(l4)
'''

#appending value to the end of list
'''print(l4)
l4.append("Hello")
print(l4)
'''
#remove
'''
l4.remove(True)
print(l4)
'''

#removing using index
'''
print(l4)
print(l4.pop(2))
print(l4)
'''

#clear whole list
'''
print(l4)
l4.clear()
print(l4)
'''

#looping list
'''for x in l4:
    print(x)
'''

#looping index in list
'''for y in range(len(l4)):
    print(y)
'''

l5=["bmw","benz","audi","tesla"]
print(l5)
#sorting alphabetically asc
'''l5.sort()
print(l5)
   '''
#sorting descending
'''l5.sort(reverse=True)
print(l5)
'''
l6=l5+l4
print(l6)
