#Problem number 20 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in



#!/usr/bin/env python
import math
print "This script generates the prime number with the index *first being the 2*"
num=int(raw_input("enter the prime number index you want\n "))
i=2
count=1
while 1:
    temp=i
    for j in range(2,int(math.sqrt(temp))+2):
        flag=0
        if temp%j==0:
            flag=1
            break
        else:
            continue
    if flag==0:
        count=count+1
    if count==num:
        break
    i=i+1
print "the %d prime number is %d" %(num,i)
