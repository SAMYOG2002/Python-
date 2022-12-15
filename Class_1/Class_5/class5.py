##STRING##
my_str = "hello world"
my_str2 = '''"hello"hello world'''

print(my_str2)
print(my_str[4])
print(my_str[5])
print(my_str[-1])
print("our" in my_str)
print("llo" in my_str)
print(my_str2.find("ll"))
print(my_str[1:10])
print(my_str[1:10:3])
print(my_str[::-1])
print(my_str.index("he"))
print(my_str.index(" "))
print(my_str.upper())
print(my_str.upper().lower())
print(my_str.capitalize())
print(my_str.title())
print(my_str + my_str2)
my_split_str = my_str.split()
my_split_str.append("---------split method")
print(my_split_str)
print(my_str.split("o"))
print(my_str.split("h"))
str_without_o = my_str.split("o")

print("o".join(str_without_o) + "       ---------    join method")  
print("+".join(str_without_o))  
print(str(str_without_o))
print("hello\"")


b = "ello"
print(b in my_str)

c = "aaa"
a = "aaabcdefaaaabababababaababaabaabbba"
print(a.count("aab"))
print(c.count("a"))
print("hello\"")