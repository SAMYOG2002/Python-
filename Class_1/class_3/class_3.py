# function check palindrome

 
# def palindrome():
#     x = input("Enter any number: ")
#     reverse = x[::-1]
#     if reverse == x:
#         print("Number is palindrome")
#     else:
#         print("Number is not palindrome")
# palindrome()


def palindrome(num):
    temp = num
    rev = 0
    while num>0:
        dig = num%10
        rev = rev*10 +dig
        print(num)
        num = num/10
        print(num)
    if temp == rev:
        print("number is palindrome")
        else:
            print("number is not paindrome")

num = input("Enter anu mumber")

        