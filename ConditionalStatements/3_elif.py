# 21. Wap to check whether the char is uppercase, lowercase, digit or special char. 

# ch=input("Enter char:")
# if 'A'<=ch<='Z':
#     print("Uppercase")   
# elif 'a'<=ch<='z':
#     print("lowercase")   

# elif '0'<=ch<='9':
#     print("digits")   
# else:
#     print("Special char")   


# 22. Wap to check whether the given integer is single digit or two digits or three  
# digits or more than three digits. 

# ch=int(input("Enter num:"))
# if 0<=ch<=9:
#     print("Single")   
# elif 10<=ch<=99:
#     print("double")   

# elif 100<=ch<=999:
#     print("three")   
# else:
#     print("more than three") 



# 23.Wap to check the given points are lying in which quadrant. 
# x=int(input("Enter point1:"))
# y=int(input("Enter point2:"))
# if x>0 and y>0:
#     print("1st")   
# elif x<0 and y>0:
#     print("2nd")   

# elif x<0 and y<0:
#     print("3rd")  
        
# elif x>0 and y<0:
#     print("4th")         
# else:
#     print("origin") 



# 24. Wap to find the greatest of 3 numbers. 
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# num3=int(input("Enter num3:"))
# if num1>=num2 and num1=>num3:
#     print("num1 is greatest",num1)   
# elif num2>=num1 and num2>=num3:
#     print("num2 is greatest",num2)            
# else:
#     print("num3 is greatest",num3) 



# 25. Wap to find the smallest of 3 numbers. 
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# num3=int(input("Enter num3:"))
# if num1<=num2 and num1<=num3:
#     print("smallest",num1)   
# elif num2<=num1 and num2<=num3:
#     print("smallest",num2)            
# else:
#     print("smallest",num3) 




# 26.Wap to check the relation between two integer numbers. 
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))

# if num1>num2:
#     print("num1 is greatter than num2")   
# elif num1<num2:
#     print("num1 is smaller than num2")            
# else:
#     print("both are equal") 




# 27. Consider a character input if it is uppercase convert it into lowercase, if it is         
# lowercase convert it into uppercase, if it is digit print the reminder when  it is 
# divided by 3 else if it is special character print it’s ASCII value. 
# ch=input("Enter char:")

# if 'A'<=ch<='Z':
#     print("Uppercase to lowercase",chr(ord(ch)+32))   
# elif 'a'<=ch<='z':
#      print("lowercase to uppercase",chr(ord(ch)-32))    

# elif '0'<=ch<='9':
#     print("it is digit and remider is",int(ch)%3)

# else:
#     print("Special char",ord(ch))  




# 28.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the    
# given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of  
# both 3 and 5.
num=int(input("Enter no:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")    
else:
    print("Invalid no")


 