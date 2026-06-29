# 11. Wap to check whether the data is mutable or not. 
# data=eval(input("enter the data:"))
# if type(data) in [list,set,dict]:
#     print("mutable data")
# else:
#     print("immutable data")

# 12. Wap to check whether the given character is digit or not. 
# ch=input("Enter the char:")
# if '0'<=ch<='9':
#     print("It is digit")
# else:
#     print("not digit")    
    


# 13. Wap to check whether the given character is special or not. 
# char=input("Enter the char:")
# if not ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
#     print("special char")
# else:
#     print("not special car")    
    

# 14. Wap to check whether a list consists of middle value or not. 
# l1=eval(input("Enyter the list:"))
# if len(l1)%2 !=0:
#     mv_index=len(l1)//2
#     mv=l1[mv_index]
#     print("list has mid value",mv)
# else:
#     print("no middle val")    

# 15. Wap to check whether the number is even or odd. 
# n=int(input("Enter the no:"))
# if n%2==0:
#     print("It is even")
# else:
#     print("odd")    
    

# 16. Wap to check whether the given data is mutable or immutable. 
# data=eval(input("enter the data:"))
# if type(data) in [list,set,dict]:
#     print("mutable data")
# else:
#     print("immutable data")

# 17. Wap to check whether 2 values are pointing to the same memory or not. 
# a=eval(input("Enter val1:"))
# b=eval(input("Enter val2:"))

# if id(a)==id(b):
#     print("Same memory add")
# else:
#     print("diff memory add")    


# 18. Consider a tuple of length 2 and check whether the tuple is homogenous or not.
# T1=eval(input("Enter the tuple:"))
# if type(T1) == tuple and len(T1) == 2:
#     if type(T1[0])==type(T1[1]):
#         print("Homogeneousn tuple")
#     else:
#         print("not homogeneous")  


# 19. Wap to check whether the string is palindrome or not. 
# s=input("enter string:")
# low_s = s.lower()
# if low_s[::-1]==low_s:
#     print("String is palindrome")
# else:
#     print("not palindrome")


# 19]B. Wap to check whether the string is palindrome or not without using slicing
# s=input("enter string:")
# low_s = s.lower()
# var=''
# for i in low_s:
#     var=i+var
# if var==low_s:
#     print("String is palindrome")
# else:
#     print("not palindrome")



# 20. Wap to check whether the number is positive or negative.
n=int(input("Enter the number:"))
if n>0:
    print("positive")
else:
    print("negative")   



