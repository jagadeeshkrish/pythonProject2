#1. Leap Year Checker:Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

def Leap_year(number):
    if (number%400==0 and number%4==0) or (number%100!=0):
        print(f"Year {number} is Leap year")
    else:
        print(f"Year {number} is not a Leap year")

Leap_year(2011)
