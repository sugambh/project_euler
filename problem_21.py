#Problem number 21 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in


#!/usr/bin/env python
import math

def amicable(x):
    i=1
    sum=0
    while i<=x/2:
        if x%i==0:
            sum=sum+i
        i=i+1
    return sum
        
print "This script calculates the sum of amicable numbers below below a specified number"
num=int(raw_input("enter the limit till which sum of amicable nu,bers has to be calculated\n"))
i=1
sum=0
while i<=num:
    temp=amicable(i)
    if((amicable(temp)==i)&(temp!=i)):
        sum=sum+i
    i=i+1
print sum
    
