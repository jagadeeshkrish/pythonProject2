#Dict
#key & Value
#name->("pramaod") mutable
#will not keep the order
my_dict={}
my_dict2={"name":"pramod","age":"45","address":"Banglore"}

print(len(my_dict2))
print(my_dict2["name"])
print(my_dict2["age"])
print(my_dict2["address"])
print(my_dict2.get("address"))
print(my_dict2.values())
print(my_dict2.keys())



phone_book=dict(name="pramod",age="45",address="Banglore")
print(phone_book)

my_dict={'a':1,'b':2,'c':3,'a':34,'d':34}
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))


for k,v in my_dict.items():
    print(k,v)
