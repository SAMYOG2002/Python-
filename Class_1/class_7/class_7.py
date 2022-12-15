###    TUPLE ###
tup1 = ("apple", "banana","mango","orange","kiwi")
tup2 = (1,2,3,"apple","mango",4,5,6,1)
#print(tup1)
#print(tup2[1:6:2])

list1 = list(tup2)
list1.append("orange")
print(list1)
tup = tuple(list1)
print(tup)
print(tup.count(1))





