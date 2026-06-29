# 29.Wap to login into the Instagram with valid username and password.(enter       
# password only if the user name is valid) 

# username='admin'
# password='pass123'

# EnterUser=input("Enter username:")
# if username==EnterUser:
#     EnterPass=input("Enter password:")
#     if password==EnterPass:
#         print("Login successful")
#     else:
#         print("Wrong password")    
# else:
#     print("Wrong Username")    
        

# 30. Wap to print the middle value of a list only if it is string. 
# lst1=[10,20,'aa',44,45]
# if (len(lst1)+1)%2==0:
#     middle=lst1[(len(lst1)//2)]
#     if type(middle)==str:
#         print("string middle value is",middle)
#     else:
#         print("middle value is not string")    
# else:
#     print("dont have middle value")

# 31.Wap to check whether the character is vowel or consonant. 
# ch=input("Enter char:")
# if 'A'<=ch<='Z' or 'a'<=ch<='z':

#     if ch in "AEIOUaeiou":
#         print("it is vowel")
#     else:
#         print("Consonent")
# else:
#     print("not alphabet")


# 32. WAP to find the greatest of 4 numbers using nested if
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a > b:
#     if a > c:
#         if a > d:
#             print("Greatest is A:", a)
#         else:
#             print("Greatest is D:", d)
#     else:
#         if c > d:
#             print("Greatest is C:", c)
#         else:
#             print("Greatest is D:", d)
# else:
#     if b > c:
#         if b > d:
#             print("Greatest is B:", b)
#         else:
#             print("Greatest is D:", d)
#     else:
#         if c > d:
#             print("Greatest is C:", c)
#         else:
#             print("Greatest is D:", d)


# 33. Wap to print the value as it is only if the length of the value is even. 
# value=input("enter value:")
# if len(value)>0:
#     if len(value)%2==0:
#         print("even val length",value)
#     else:
#         print("length of val is odd")    
# else:
#     print("invalid")

# 34.Wap to print the last value of a list only if it is palindrome string starting with  vowel. 

# lst1=['aas',20,387,'cabac']
# lv=lst1[-1]
# if type(lv)==str:
#     if lv==lv[::-1]:
#         if lv[0] in 'AEIOUaeiou':
#             print("it is palindrome starting with vowel:",lv)
#         else:
#             print("it is palindrome but not start with vowel")    
#     else:
#         print("not palindrome")
# else:
    
#     print("not string")

    
    
    
# 35.Wap to print the reversed string only if it is starting with vowel ,ending with     
#  consonant and having a middle value. 
# data=input("enter string:")

# if data[0] in 'AEIOUaeiou':
#     is_letter=(('A'<=data[-1]<='Z') or ('a'<=data[-1]<='z'))
#     is_consonent=(data[-1] not in 'AEIOUaeiou')
#     if is_consonent and is_letter:
#         if len(data)%2==1:
#             print("it has middle value so rev the string:",data[::-1])
#         else:
#             print("not have middle value")    
#     else:
#         print("ending is not with consonent or not alpha")
# else:
#     print("start not with vowel")



# 36.Wap to find the second greatest of 4 values. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a>b and a>c and a>d:
#     if b>c and b>d:
#         print("second greatest is b",b)
#     elif c>d:
#         print("second greates is c",c)   
#     else:
#         print("second greates is d",d)
# elif b>a and b>c and b>d:
#     if a>c and a>d:
#         print("second greatest is a",a)
#     elif c>d:
#         print("second greates is c",c)   
#     else:
#         print("second greates is d",d)
# elif c>b and c>a and c>d:
#     if b>a and b>d:
#         print("second greatest is b",b)
#     elif a>d:
#         print("second greates is a",a)   
#     else:
#         print("second greates is d",d)
# else:
#     if b>c and b>a:
#         print("second greatest is b",b)
#     elif c>a:
#         print("second greates is c",c)   
#     else:
#         print("second greates is a",a)

# 37.Wap to find the smallest of 4 numbers. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a < b:
#     if a < c:
#         if a < d:
#             print("smallest is A:", a)
#         else:
#             print("smallest is D:", d)
#     else:
#         if c < d:
#             print("smallest is C:", c)
#         else:
#             print("smallest is D:", d)
# else:
#     if b < c:
#         if b < d:
#             print("smallest is B:", b)
#         else:
#             print("smallest is D:", d)
#     else:
#         if c < d:
#             print("smallest is C:", c)
#         else:
#             print("smallest is D:", d)



# 38. Write a program to print middle Character of the given string only if it is upper                
#     Case Character. 
str1='abBcd'
if type(str1)==str:
    if len(str1)%2==1:
        if 'A'<=str1[len(str1)//2] <='Z':
            print("middleval",str1[len(str1)//2])
        else:
            print("middle val is not uppercase char")    
    else:
        print("dont have middle char") 
else:
    print("not strinf")               
            
            