numbers=[1,2,3] #collection of items

def do_something(numbers):
    numbers.append(4)  #[100,1,2,3]
    numbers[0]=100
    return numbers

l=do_something(numbers)
print(l)
numbers.append(10)
print(l)