#Explain the difference between the = operator and the == operator in Python.
# = operator is an assignment operator that is used to assign a variable Example:
a=2 #2 is assigned to variable a
print(a)

# == operator is used for compare and check that the variables are equal or not

b,c=3,3
print(b==c) #True as b & c are equal
b,c=3,4
print(b==c) #False as b & c are not equal

#What does the ** operator do in Python, and how is it used?
# ** operator is used to get the power of the given variable;Example:
d= 2**3 #2*2*2
print(d)


#What does the ^ operator do in Python, and in what context is it commonly used?
# ^ is a bitwise XOR operator that is used to compare each bit of different variables and set the bit to 1 if either bits different & sets the bit to 0 if both the bits are same
#Example
e=4  #100
f=5  #101
print(e^f) #001

#Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
def calculate_square_cube(number):
    square=number**2
    cube=number**3
    return square,cube

number = float(input("Enter a number: "))

square, cube = calculate_square_cube(number)

print(f"The square of {number} is {square}")

print(f"The cube of {number} is {cube}")
