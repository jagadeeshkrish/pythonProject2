#SET
#Collection of items
list_of_unique_items={1,2,3,4,4,5,5}
print(list_of_unique_items)

list1=[45.2,33,33,45,21]
set1=set(list1)
print(set1)
print(len(set1))

#intersection & Union
set1={1,2,3}
set2={4,5,6}
set3=set1.union(set2)
print(set3)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.intersection(set2) #gives common data
print(set3)
set3=set1.difference(set2)
print(set3)
set3=set2.difference(set1)
print(set3)

set1={1,2,3,4,5}
set2={2,3,4}
subset=set2.issubset(set1)
print(subset)
set1={1,2,3,4,5}
set2={2,3,8}
subset=set2.issubset(set1)
print(subset)

set1=set(["TheTestacademy","For","TheTestacademy."])
print(len(set1))
for i in set1:
    print(i)

set1=set([1,2,3,4,5,6,7,8,9,10,11])
print(len(set1))
set1.remove(5)
print(len(set1))
print(set1)
