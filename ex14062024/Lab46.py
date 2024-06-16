#Pass some information to the f(n)
def greet (name): #name- parameter or argument
    print("Hello")

greet("krishna")
greet(123)

def allowed_to_enter_class(name):
    match name:
        case "DELL":
            print("Dell is allowed")
        case "Subham":
            print("subham is allowed")
        case _:
            print("Not allowed")

allowed_to_enter_class("DELL")
allowed_to_enter_class(123)