#dictionary datastructure
#key,value pair
#key will be unique but we can change the value
#duplicate not accepted in key
stu={
"Name":"Abc",
"Age":50,
"College":"VTU",
"Age":70
}
'''print(stu)
print(type(stu))
print(len(stu))'''

#multiple items inside dictionary
'''
stu={
"Name":"Abc",
"Age":50,
"College":"VTU",
"Age":70
}
print(stu)
print(type(stu))
allk=stu.keys()
print(allk)

alls=stu.values()
print(alls)

stu["College"]="hello"
print(stu)
'''
#looping dict(keys,values,items)
'''for i,y in stu.items():
    print(i,y)'''

#update(.update())

#remove(.pop(),.popitem(),del,clear())
'''stu.pop("College")
print(stu)'''

stu.popitem()
print(stu)


