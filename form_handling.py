#file handling

#creating new file
'''
f=open("D:\internship 2026\myfile.txt","x")
'''

#creating file with exception handling
'''
try:
    f=open("D:\internship 2026\myfile.txt","x")
except:
    print("File already exist")
'''

#creating file using different approach
'''
with open("D:\internship 2026\myfile.txt","x"):
    print("File created")
'''

#file reading
'''
f=open("D:\internship 2026\myfile.txt","r")
print(f.read())
f.close()
'''
'''
f=None
try:
    f=open("D:\internship 2026\myfile.txt","r")
    print(f.read())
except:
    print("Could not read file")
finally:
    if f is  not None:
        f.close()
'''

#file writing without appending
'''
a="this is python traing..."
with open("D:\internship 2026\myfile.txt","w")as fos:
    fos.write(a)
with open("D:\internship 2026\myfile.txt","a")as fos:
    fos.write(a)
with open("D:\internship 2026\myfile.txt","r")as fos:
    print(fos.read())
'''

import os
#os.mkdir("D:\internship 2026\temp")#create folder in the given path
#os.removedirs("D:\internship 2026")#remove
os.remove("D:\internship 2026\myfile.txt")

print("Done")
