n=5

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

#n=5

for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")
#n=5
ascii_value= 65
for i in range(n):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet,end=" ")

    ascii_value +=1
    print("\n")


for i in range(n):
    for j in range(n):
        print("*", end=" ")

    print("\n")
    n = n - 1