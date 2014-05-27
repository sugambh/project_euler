#Problem number 92 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
num=int(raw_input("enter the limit")) 
i=1
count=0
while i<num :
    temp=i
    while temp!=1|temp!=89:
        s=str(temp)
        digits=len(s)
        sum=0
        for j in range(0,digits):
            sum=sum+pow(int(s[j]),2)
        temp=sum
        print temp,
    print
    if i==89:
        count=count+1
    i=i+1
print count
            
