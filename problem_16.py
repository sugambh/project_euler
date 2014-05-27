#Problem number 16 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

#!/usr/bin/env python
base=int(raw_input("give the base "))
exponent=int(raw_input("give the  power "))
a=pow(base,exponent)
b=str(a)
sum=0
for i in range(len(b)):
    sum =sum+int(b[i])
print sum
