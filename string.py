#string

#string for single line initialisation
'''name="arun"
print(name)
print(type(name))'''

#string for multi-line initialisation
address='''
715 Bmr layout
fbejwfhbiweohfnowe
fewbjkfbwjefblkwe'''
#print(address)
#print(type(address))


#slicing
'''txt="hello how are you guys"
data=txt[5:] #how are you guys
print(data)

data=txt[:4]
print(data)

data=txt[:5]
print(data)

data=txt[-6:-2]
print(data)


'''

#modifiers
'''
txt="How are you"
print(txt.upper())
print(txt.lower())

'''
#strip
'''txt="...........,,,,,,,,,,How are you"
print(txt.strip("."))
'''

#replace
'''txt="How are you"
data=txt.replace("How","What")
print(data)
'''
#split
'''txt="hello arun, this is from mindset"
data=txt.split(",")
print(data)
print(type(data))
print(data[0])'''


#concatination
'''a="hello"
b=" bye"
c=a+" I am rahul ok "+b
print(c)
'''
'''
x="10"
y="5"
print(x+y)
a=int(x)
b=int(y)
print(a+b)
'''

#formating (f)
'''age=25
#print("i am arun and my age is ",age)
txt=f"hello i am arun my age is {age}"
print(txt)
'''
'''
price=102.983
txt=f"price is {price:.2f}"
print(txt)
'''

#escape character
#\" \' \n \b
'''txt="\"hello mr\""
print(txt)
txt1="\'hello mr\'"
print(txt1)

txt2="hello bro\nwhat r u doing"
print(txt2)
'''

txt="hello world hello"
#print(txt.capitalize())

#print("hello".casefold())

#print(txt.title())

#print(txt.islower())

#print(txt.isupper())

#print(txt.find("world"))

#print(txt.count("hello"))

#print(txt.startswith("hello"))

#print("123num".isalnum())

#print("123".isdigit())


