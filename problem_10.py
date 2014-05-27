#Problem number 10 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
num=int(raw_input("enter the number"))
array=range(2,num+1)
a=dict([(x, 1) for x in array])
for i in array:
    if a[i]==1:
        for j in range(pow(i,2),num+1,i):
            a[j]=0

sum=0
for i in array:
    if a[i]==1:
        #print i
        sum=sum + i
print sum
