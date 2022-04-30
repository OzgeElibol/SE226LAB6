import random

#1
def lambdafunc(n):
 f=lambda x:(x-3)/(x*x)
 list=[]
 for a in range(1,n+1):
    list.append(f(a))
 print(sum(list))

n=int(input("Please enter a n integer: "))
lambdafunc(n)

#2
def func2(n):
    """The function calculates and prints the result of the equation using a recursive function"""
    if n==0:
        return 1
    else:
        return (((n/(n+2))-10)*func2(n-1))

n=int(input("Please enter a number: "))
print(func2(n))
print(func2.__doc__)
