my_list = [1,2,3,4,5,6,7,8,9,10]
next_list = my_list[::-1]
list_1 = list(zip(my_list, next_list))

def sum_of_num(a,b):
    return a+b

print(sum_of_num(1,2))
sum = map(sum_of_num, my_list, next_list)
print(list(sum))
print(list_1)


