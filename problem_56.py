#Problem number 56 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
num=int(raw_input("enter the limit"))
max1=0
for a in range(1,num):
    for b in range(1,num):
        x=pow(a,b)
        y=str(x)
        sum1=0
        for i in range(0,len(y)):
            sum1=sum1+int(y[i])
        if(sum1>max1):
            max1=sum1
print max1
        
            
