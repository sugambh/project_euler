#Problem number 29 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
num=int(raw_input("enter the number\n"))
array=range(2,num+1)

k=range(0,(num-1)*(num-1))
i=0
max=0
for a in array:
    for b in array:
        k[i]=pow(a,b)
        if k[i]> max:
            max=k[i]
        i=i+1
p
#print max
#z=range(0,max+1)
#print z
#for l in k:
#    z[l]=1
#print z
#for o in range(0,max):
#    if z[o]==1:
#        print o
    

