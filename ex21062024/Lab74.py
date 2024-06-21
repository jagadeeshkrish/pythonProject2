#Decorator
#it is a function which takes an another function as a argument &
# returns a new function that usually extends

def my_decorator(func):
    def wrapper():
        print("starting....")
        print("************")
        func()
        print("************")
        print("Ending")
    return wrapper()
@my_decorator
def say_hello():
    print("Say Hello")

import time

def note_time_decorator(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time = time.time()
        print("Time Taken "+str(end_time-start_time))
    return  wrapper()

@note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the logs of time taken")

@note_time_decorator
def reporting_function():
    time.sleep(5)
    print("print the logs of time taken")

