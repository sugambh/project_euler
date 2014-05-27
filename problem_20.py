#Problem number 20 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
def fact(x):
    if(x==1):
        return x
    else:
        return x*fact(x-1)
print "this script can calculate the sum of digits  of factorial of any number"
num=int(raw_input("enter the number"))
factorial=fact(num)
temp=str(factorial)
sum_of_the_digits=0
for i in range(len(temp)):
    sum_of_the_digits+=int(temp[i])
print "the sum is %d" %(sum_of_the_digits)
    
