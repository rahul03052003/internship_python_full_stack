#regex module

'''import re
psw=input("Enter password :")
#password pattern matching for strong password(atleast 1cap, 1 sm, 1 digit, len 8)
reg=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

pat=re.compile(reg)

match=re.search(pat,psw)
if match:
    print("Password accepted")
else:
    print("Password is wrong")

'''

#assignment it to check for special charcter
import re

psw = input("Enter password: ")

# Added (?=.*[@$!%*?&]) for special characters
reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.fullmatch(reg, psw):
    print("Strong password accepted!")
else:
    print("Password is too weak. Ensure it has caps, numbers, and special chars.")
