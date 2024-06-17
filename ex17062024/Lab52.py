def f1(a,b,c):
    return a+b+c #irrespective of data type data will return result

result=f1(3,4,5)
print(result)
result=f1(a=4,b=6,c=8)
print(result)
result=f1(a=12,c=6,b=9) #name is to be given if we change order
print(result)
print(f1(a=15,c=6,b=9))