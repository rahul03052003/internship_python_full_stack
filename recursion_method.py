#recursion
#we need to write termination logic in recursion
#calling itself again and again
'''def display(n):
    print(n)
    if n==1:
        return 1
    return display(n-1)

display(10)'''

def fact(n):
    print(n,"X",end=" ")
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
