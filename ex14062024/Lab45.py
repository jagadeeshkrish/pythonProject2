#Multiple conditions
#Switch
#Match Case  keyword to match the case
number=int(input("Enter a number\n"))
match number:
    case 1:
        print("Hello 1")
    case 2:
        print("Hello 2")
    case 3:
        print("Hello 3")
    case 4:
        print("Hello 4")
    case _:
        print("No  idea")

number=(input("Enter your name\n"))
match number:
    case "krishna":
        print("you are krishna")
    case _:
        print("No idea")