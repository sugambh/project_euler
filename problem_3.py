#Problem number 3 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
import math
print "This script calculates the largest prime factor of the entered number"
num=int(raw_input("Enter the Number\n"))
for i in range(2,int(math.sqrt(num))+2):
   # print "*",i,"*"
    if num%i==0:
        flag=0
        temp=i
        for j in range(2,int(math.sqrt(temp))+2):
            if temp%j==0:
                flag=1
        if flag==0:
            print i                
    else:
        continue
