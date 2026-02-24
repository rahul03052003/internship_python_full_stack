#random module

import random

#generating randome number from given range
'''x=random.randrange(4,10)
print(x)'''

#generating otp

'''num=0
otp=""
for r in range(4):
    num +=random.randrange(2,10)
    otp+=str(num)
    #print(otp)
print(otp,end="\n")
'''

#choice

'''li=["volvo","benz","susuki","kia"]
ch=random.choice(li)
print(ch)
print(type(ch))'''

#choices

li=["volvo","benz","susuki","kia"]
ch=random.choices(li,k=3)
print(ch)
print(type(ch))



