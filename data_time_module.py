from datetime import datetime

x=datetime.now()  #2026-02-24 15:05:04.690367
'''print(x,end="\n")
#get only year
print(x.year)
print(x.month)
print(x.date())
'''
#strings format time
print(x.strftime("%a"))
print(x.strftime("%Y"))
