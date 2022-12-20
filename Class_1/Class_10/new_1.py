my_list = [1,2,3,4,5,6,7,8,9,10]
next_list = my_list[::-1]
new_list = list(map(lambda x,y : x+y , my_list , next_list))
def check_even(num):
      if num%2 == 0:
          return True
      else:
         return False
              
new_list =list(filter(lambda x: x%2 == 0, my_list))
list2 = list(filter(lambda x: x%2 == 1, my_list))



print(new_list)
print(list2)

