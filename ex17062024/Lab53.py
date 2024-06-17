# *args :can add any number of arguments
print("pramod","JK","NK")

def sum3(a,b,c):
    return a+b+c

result1=sum3(2,3,4)
result2=sum3(a=1,b=2,c=6 )
print(result1)
print(result2)

def print_arguments(*args):  #args is nothing but a list
    for i in args:
        print(i,end="\n")

print_arguments("Lucky","amit","JK")

a=["pramod","amit","JK"]
for i in a:
    print(i)
