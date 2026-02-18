#set - {}
#no indexing
#sets are immutable(we can't change the values)(unordered,unindexed,unchangeable)
#hashing - Dynamic values of memory  is generated(different output)
#No duplicate values will be allowed

s1={"apple","mango","papaya","guvava"}
'''print(s1)'''

s2={True,"hello","bye","hello",20,"mango"}
'''print(s2)'''

#looping set
'''for x in s2:
    print(x)'''

#adding set and list values
'''l1=["hi","python",50,"bye"]
s2.update(l1)
print(s2)'''

#join two sets union method(new set with all items)(|)

'''s3=s1.union(s2)
print(s3)

s5=s1|s2|s3
print(s5)'''

#intersection of sets(return only the common in the sets)
'''s4=s1.intersection(s2)
print(s4)
'''

'''s6={"car","bike","train"}
s7={"car","aeroplane","bycycle"}
s8=s6.intersection(s7)
print(s8)
'''
#alternative for intersection{&}
s6={"car","bike","train"}
s7={"car","aeroplane","bycycle"}
'''s8=s6&s7
print(s8)'''

#intersection_update():modifies the variable instead returing new variable
'''print(s6)
s6.intersection_update(s7)
print(s6)'''

#difference() will return a new set that will contain only the,
#items from the first set that are not present in other

'''s8=s6.difference(s7)
print(s8)'''
#alternate for difference method is(-)

'''s8=s6-s7
print(s8)'''

#symmetric_difference()(^)
'''s8=s6.symmetric_difference(s7)
print(s8)'''

#removing set values(.discard,.pop,.remove)
'''print(s6)
s6.discard("car")
print(s6)
'''
s6.pop()
'''print(s6)'''

#clearing values from the set
s6.clear()
'''print(s6)'''

#using del keyword to delete set(s6 itself will be deleted)
del s6
'''print(s6)'''








