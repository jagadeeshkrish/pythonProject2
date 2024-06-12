#Conditions & Loop
#gae>18->you area allowed to go for voting
#age<18-> you are not allowed

#if condition:
#    code to be executed
#else:
#    code to be executed when if conditioin is false

age=int(input("Enter your age "))
if age>18:
    print("allowed")
else:
    print("Not allowed")

a=8
if 8==5:
    print("Hello")
else:
    print("Bye")


a=50
b=45
x=10
y=67
result1=(a>b) #False
result2=(x<y) #True
result3=result1 and result2  #False and True
print(result3) #False