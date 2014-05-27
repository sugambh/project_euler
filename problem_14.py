#Problem number 14 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
print "solution for  problem 14"
i=1
max=1
x=1
while i<=1000000:
    num=i
    count=1
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
        count=count+1
    #print i,count
    if(count>max):
        x=i
        max=count
    i=i+1
print max,x
