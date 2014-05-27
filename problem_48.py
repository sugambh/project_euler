#Problem number 25 ,project euler
#Script contributed by  Sugam Anand
#Website :www.sugamanand.in

print "This script calculates the sum of the num to the power num series "
num=int(raw_input("enter the number"))
i=1
sum=0
while i<=num:
        sum=sum+pow(i,i)
        i=i+1
sum=str(sum)
digit=len(sum)
array= range(digit-10,digit)
for i in array:
    print sum[i],
print 
    
