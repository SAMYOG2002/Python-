my_list = [1,2,3,4,5,6,7,8,9,10]
next_list = my_list[::-1]


take = str(input("Enter odd or even: "))
new_list =list(filter(lambda x: x%2 == 0, my_list))
list2 = list(filter(lambda x: x%2 == 1, my_list))

if take == 'even':
    print(new_list)
elif take == 'odd':
    print(list2)

