#Provide the three inputs and the number to compare and it will give the combinations where the sum is not equal to N.

from itertools import product

x=int(input())
y=int(input())
z=int(input())
n=int(input())

def GeneratePermuation(x,y,z):
    result = [list(i) for i in product(range(x+1),range(y+1),range(z+1))]
    return result

PermuationGenerated=GeneratePermuation(x,y,z)

def Checker(values,n):
    final=[]
    for upperValue in values:
        temp=0
        for innervalue in upperValue:
            temp=temp+innervalue
        if temp!=n:
            final.append(upperValue)   
    print(final)            

Checker(PermuationGenerated,n)