#not operatoe is always used with boolean True or False
#how to doble the existing list
list=[1,2,3,4,5]
temp_list=[]
for i in list:
    temp=i*2
    temp_list.append(temp)
print(temp_list)

def double_item(num):
    return num*2
double_item=lambda num:num**2
#Map()
#Takes each item from the list
#execute the function on it
#return same number of elements(list)
my_list=[1,2,3,4,5]
double_list=list(map(double_item,my_list))
print(double_list)