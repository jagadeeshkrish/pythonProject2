#Important question
#Lambda expression
#to do task in one line

def double_my_salary(salary):
    return salary*2
new_salary=double_my_salary(100)
print(new_salary)

f_double_salary=lambda salary:salary*2
print(f_double_salary(100))

def sum_two(a,b):
    return a+b
o=sum_two(3,4)  #define a variable
print(o)

name=lambda a,b:a+b
print(name(3,4))

def sum_three(a,b,c):
    return a+b+c
o=sum_three(3,4,5)
print(o)

o_a=lambda a,b,c:a+b+c
print(o_a(3,4,5))
