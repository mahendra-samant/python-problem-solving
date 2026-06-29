# # 39.Wap to print python for 5 times. 
# i=0
# while i<5:
#     print("python")
#     i+=1


# # 40.Wap to print n natural numbers. 
# n=int(input("enter the no:"))
# i=1
# while i<=n:
#     print(i)
#     i+=1


# # 41.Wap to print multiplication table for n. 
# n=int(input("enter the no:"))
# i=1
# while i<=10:
#     print(f"{n} x {i}={n*i}")
#     i+=1


# # 42.Wap to find the sum of n natural numbers. 
# n=int(input("enter the no:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


# # 43. Wap to find the product of n natural numbers or factorial of a number. 
# n=int(input("enter the no:"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print(fact)

# # 44.Wap to print all the characters of a string. 
# str1=input("Enter string :")
# i=0
# while i<len(str1):
#     print(str1[i])
#     i+=1


# # 45.Wap to print all the characters present at even index of a string. 
# str1=input("Enter string :")
# i=0
# while i<len(str1):
#     if i%2==0:
#         print(str1[i])
#     i+=1    


# # 46.Wap to extract all the lowercase characters present in a string. 
# str1=input("Enter string :")
# i=0
# while i<len(str1):
#     if 'a'<=str1[i]<'z':
#         print(str1[i])
#     i+=1  


# # 47.Wap to extract all the vowels present in a string. 
# str1=input("Enter string :")
# i=0
# while i<len(str1):
#     if str1[i] in 'AEIOUaeiou':
#         print(str1[i])
#     i+=1  




# # 48.Wap to print factors of a integer number. 
# n=int(input("enter no:"))
# i=1
# while i<n:
#     if n%i==0:
#         print(i)
#     i+=1    



# # 49.Wap to toggle a string. 
# str1=input("Enter string :")
# i=0
# toggle=''
# while i<len(str1):
#     if 'A'<=str1[i] <='Z':
#         toggle+=chr(ord(str1[i])+32)
#     elif 'a'<=str1[i] <='z':
#         toggle+=chr(ord(str1[i])-32)
#     else :       
#      toggle+=str1[i]
#     i+=1
# print(toggle)        


# # 50.Wap to reverse the given number. 
# n=int(input("enter the no:"))
# rev=0
# while n!=0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)    


# # 51.Wap to find the sum of individual digits of a number. 
# n=int(input("enter the no:"))
# sum=0
# while n!=0:
#     ld=n%10
#     sum+=ld
#     n=n//10
# print(sum)



# # 52. Wap to check whether the number is perfect or not.
# n=int(input("enter the no: "))
# sum1=0
# i=1
# while i<n:
#     if n % i==0:
#         sum1+=i
#     i+=1    
# if sum1==n:    
#     print(f"The number {n} is perfect")
# else:
#     print(f"The number {n} is not perfect")    
 



# 53.Wap to login to phonepe by entering correct otp.
otp=int(input("Enter the OTP :"))
originalOTP=123456

while otp!= originalOTP:
    print("Please enter the valid OTP!!")
    otp=int(input("Enter the OTP :"))

print("Login to phonePe successfully!!")    
    







