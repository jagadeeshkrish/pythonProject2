#Tuple
#Decorators

#Real case where we use tuple
#URLs which doesn't change much
ENV_API_URL=tuple("abc.com/get","xyz.com/post",)
print(ENV_API_URL)

t=tuple()
print(t)
#conversion of list to tuple
t1=tuple(["promod","amit","manish"])
print(t1)

del t1

h1=("a","b")
h2=("c","d")
new_t=(h1,h2)
print(new_t)
print(new_t[0])
print(new_t[1])
print(new_t[0][0])
print(new_t[1][1])

#Unpacking of the tuple
a,b,c=(12,13,14)

t=(12,13,14)
#t.append() #tuple are immutable in nature
new_t=t+(4,)
print(new_t)

my_list=list(t)
print(my_list)
my_list.append(5)
new_t2 =tuple(my_list)
print(new_t2)