#print()
# self - Concept in opps which points to inself -ignore
# * args  - unlimited number of arguments *
# sep ='' -How you want to seperate the arguments
# end='\n' - in the end what you want to do
# file= None - File IO

print("Hello","World",123,True,3.14,sep="-")
print("Hello","World",123,True,3.14,sep="*")
print("Hello","World",123,True,3.14,sep=" ")
print("Hi,My name is Jagadeesh","Krishna",sep=" ")
print("Hi,My name is Jagadeesh","Krishna",end="\n")
print("Hi","Jagadeesh","Krishna",sep="_",end="\t")
print("Hi","My name is",end='-')
print("Jagadeesh")

print(max(10,20))
age =33  #Dynamic type
print(type(age))
age="thirty three"
print(type(age))
name="Jagadeesh"
print(type(name))

a,b,c=10,20,30
print(a+b+c)
name=input("Enter your name ")
print("Your name is",name)