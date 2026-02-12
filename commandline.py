#command line
'''import sys
print(sys.argv)
name=sys.argv[1]
age=sys.argv[2]
print("Entered name is: ",name)
print("Age is: ",age)
'''
#python commandline.py --h
import argparse
p=argparse.ArgumentParser()
p.add_argument("Name")
p.add_argument("age")
args=p.parse_args()
print(args.Name)
print(args.age)
