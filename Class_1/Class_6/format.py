str = "Hello world form new python script"
a = "Ram Bahadur"
b = f"My name is {a} {str}"
c = " {2},{1},{0}".format(a,str,b)
my_string = str.replace("w","a") # Replaces the w with a in the string
print(b)
#print(c)
print (my_string)
my_list = str.split(" ")
print(my_list)
for index, item in enumerate(my_list):
    if index % 2 == 0:
        my_list[index] = item.upper()
    #print(index, item)
print(my_list)