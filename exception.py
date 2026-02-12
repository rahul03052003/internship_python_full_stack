#exception hanling
a=10
b=10

'''c=a/b
print("Division result is: ",c)
print("Inside except block")
c=a+b
print("Addition result is: ",c)
'''
'''
d=0
try:
    c=a/d
    print("Division result is: ",c)
except ZeroDivisionError:
    print("Inside except block")
    c=a+b
    print("Addition result is: ",c)
'''
d=[10,20,30]
'''
try:
    print(d[4])
except IndexError:
    print("Inside error")
print("Done")
'''
try:
    print(d[3])
except IndexError:
    print("Inside except")
else:
    print("Inside else")
finally:
    print("Inside finally block")
