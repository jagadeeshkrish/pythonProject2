#Function is a block of code that is executed anx can be reused; will have definition and call
#Built in Functions-builtins.py-fines in (python3 setup)
#which are created by pthhon contributors

def say_hello(): #NO RETURN TYPE  & NO PARAMETER
    print("Hello")

def say_hello_arg(name): #NO RETURN TYPE  & WITH PARAMETER
    print("Hello",name)

say_hello()
say_hello_arg("Krishna")

def say_hello_arg_default(name="JAGADEESH"): #NO RETURN TYPE  & WITH  DEFAULT ARGUMENT
    print("Hello",name)

say_hello_arg_default()
say_hello_arg_default("Krishna")
say_hello_arg_default(name="jk")

def sum_number_argument_ret(a,b):
    return a+b
#result=sum_number_argument_ret

#sum_number_argument_ret(3, 4)
#result=sum_number_argument_ret(a:31,b:43)

