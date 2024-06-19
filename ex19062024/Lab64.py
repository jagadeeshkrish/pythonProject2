#lambda arguments:exprression

def find_odd_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

find_odd_even(5)

check_even_odd=(lambda num:"Even" if num%2==0 else "odd") (8)
print(check_even_odd)

power_function= lambda:int(input("Enter the number"))
result=power_function()
print(result)