#Factorial
import math
n=5
factorial=1
result= math.factorial(5)
print(result)


for i in range(1,n+1):
    factorial=factorial*i

print(factorial)

factorial=1
while n>0:
    factorial = factorial*n
    n=n-1

print(factorial)