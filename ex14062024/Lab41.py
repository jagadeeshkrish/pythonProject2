#For loop

for counter in range (0,101): #0-99
    print(counter)
for counter in range (0,101,2):#even
    print(counter)
for counter in range (1,101,2):#odd
    print(counter)
for counter in range (0,101,3):#3 multiple
    print(counter)

for counter in range (1,101): #0-99
    print(counter)
    if counter==5:
        break
print("Outside of the program")