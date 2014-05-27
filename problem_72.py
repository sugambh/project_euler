#Problem number 72 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in
def gcd(a,b):
    if b>a:
        temp=b
        b=a
        a=temp
    if b==0:
        return a
    else:
        return gcd(b,a%b)
#!/usr/bin/env python
num=int(raw_input("enter the number\n"))
x=int(raw_input("enter the numerator\n"))
y=int(raw_input("enter the denominator\n"))
fraction=float(x)/float(y)
count=0
for d in range(1,num+1):
    for n in range(1,d):
        if gcd(d,n)==1:
            count=count+1
            
print count
