#program to find max between to numbers

a=int(input("Enter num1 \n"))
b=int(input("Enter num2 \n"))

if a>b:
    print(a)
else:
    print(b)

#multiple conditions
num1=int(input("Enter num1 \n"))
num2=int(input("Enter num2 \n"))
num3=int(input("Enter num3 \n"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
#outtrue if condition else outfalse