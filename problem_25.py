#Problem number 25 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in


#!/usr/bin/env python
def fibonaccci(x):
    temp1=1
    temp2=1
    sum=0
    for i in range(3,x+1):
        sum=temp1+temp2
        temp1=temp2
        temp2=sum
    return sum
        
print "this script calculates the first term to have 1000 digits in fibonacci sequence "
digit=int(raw_input("enter the digit ,you want to check  fibonacci term for !"))
i=3
while 1:
    if len(str(fibonaccci(i)))==digit:
        print i#,fibonaccci(i)
        break
    i=i+1
