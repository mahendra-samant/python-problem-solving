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
 



# # 53.Wap to login to phonepe by entering correct otp.
# otp=int(input("Enter the OTP :"))
# originalOTP=123456

# while otp!= originalOTP:
#     print("Please enter the valid OTP!!")
#     otp=int(input("Enter the OTP :"))

# print("Login to phonePe successfully!!")    
    




# # 54.Wap to run infinite loop until user enters the correct password. 
#1way
# password='pass@123'
# temp=True

# while temp:
#     pwd=input("Enter the password :")
#     if pwd==password:
#         print("correct password")
#         temp=False
#     else:
#         print("Enter agian")    

#2way
# password='pass@123'


# while True:
#     pwd=input("Enter the password :")
#     if pwd==password:
#         print("correct password")
#         break
#     else:
#         print("Enter agian")  
 
#3way
# password='pass@123'
# pwd=" "

# while pwd!=password:
#     pwd=input("Enter the password :")
#     if pwd!=password:
#         print("Enter agian")
# print("correct password")       
       
          



# # 55.Wap to extaract all the even integers present in a tuple at odd index. 
# tup1=(10,30,41,50,61,81)
# out=[]
# i=0
# while i<len(tup1):
#     if i%2 !=0 and tup1[i] % 2 == 0:
#         out.append(tup1[i])
#     i+=1
# print("ans is",out)            


# # 56.Wap to remove duplicates from a list without converting into set.
# lst1=[10,20,30,50,50,30] 
# out=[]
# i=0
# while i<len(lst1):
#     if lst1[i] not in out :
#         out.append(lst1[i])
#     i+=1    
# print("list without duplicates",out)


# # 57.Wap to find the sum of all the odd numbers between the given range. 
# startNo=int(input("Enter starting number:"))
# endNo=int(input("Enter ending number:"))
# if startNo<endNo:
#     i=startNo
#     total=0
#     while i<=endNo:
#         if i%2!=0:
#             total+=i
#         i+=1
#     print(f"sum of odd numbers between {startNo} and {endNo} is {total}")
    
# else:
#     print("starting number must be lower than ending number")    


# # 58.Wap to find the greatest number in a given list of integers. 
# 1way
# import sys
# lst58=[10,-34,89,32,-99,0]
# greatest=-sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]>greatest:
#         greatest=lst58[i]
#     i+=1    
# print("the greatest no is ",greatest)

#2way
# lst58=[10,-34,89,32,-99,0]
# greatest=lst58[0]
# i=1
# while i<len(lst58):
#     if lst58[i]>greatest:
#         greatest=lst58[i]
#     i+=1    
# print("the greatest no is ",greatest)


#58.1 .Wap to find the 2nd greatest number in a given list of integers.
# import sys
# lst58=[10,-34,89,32,-99,0]
# greatest=-sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]>greatest:
#         greatest=lst58[i]
#     i+=1    
# sec_great=-sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]>sec_great and lst58[i]<greatest:
#         sec_great=lst58[i]
#     i+=1 
# print("the 2nd greatest no is ",sec_great)        



# # 58.2.Wap to find the smallest number in a given list of integers. 
# import sys
# lst58=[10,-34,89,32,-99,0]
# smallest=sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]<smallest:
#         smallest=lst58[i]
#     i+=1    
# print("the smallest no is ",smallest)


# # 58.3 .Wap to find the 2nd smallest number in a given list of integers.
# import sys
# lst58=[10,-34,89,32,-99,0]
# smallest=sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]<smallest:
#         smallest=lst58[i]
#     i+=1    
# sec_small=sys.maxsize
# i=0
# while i<len(lst58):
#     if lst58[i]<sec_small and lst58[i]>smallest:
#         sec_small=lst58[i]
#     i+=1 
# print("the 2nd greatest no is ",sec_small)        



# # 59.Wap to find the sum of cube of a number in a string. 
# str59="python@3&8"
# total=0
# i=0
# while i<len(str59):
#     if "0"<= str59[i] <="9":
#         total+=(ord(str59[i])-48)**3
#     i+=1    
# print("the sum of cube of nos is ",total)


# # 60.Wap to check whether the number is Armstrong or not. 
# n=int(input("enter the no:"))
# temp=str(n)
# total=0
# count=0
# for i in temp:
#     count+=1
# while n!=0:
#     ld=n%10
#     total=total+(ld**count)
#     n=n//10
# if total==int(temp):
#     print(f"Number {int(temp)} is Armstrong")   
# else:     
#     print(f"Number {int(temp)} is not an Armstrong")  
     
     

# # 61.Wap to get the following output. 
# #     A=’10011100’   B=’00110101’    out=4(count of positions having same values) 
# A="10011100"
# B="00110101"
# count=0
# i=0
# while i<len(A):
#     if A[i]==B[i]:
#         count+=1
#     i+=1    
# print("count is ",count)



# # 62.Wap to check the given number is prime or not. 
# n=int(input("Enter the number:"))
# isPrime = True
# i=2
# if n>1:
#     while i<n:
#         if n % i == 0:
#             isPrime=False
#         i+=1  
            
                
#     if isPrime==True:
#         print(f"{n} is prime number")
#     else:
#         print(f"{n} is not prime number")    
# else:
#     print(f"{n} is not a prime number")


# # 63.Wap  to check whether the number is palindrome or not. 
# #1way
# n=int(input("Enter the number:"))
# temp=n
# rev=0
# while n!=0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if rev==temp:
#     print(f"The number {temp} is palindrome")    
# else:
#     print(f"The number {temp} is not palindrome")  

# #2way
# n=int(input("Enter the number:"))
# s=str(n)
# if s[::-1]==s:
#     print(f"The number {s} is palindrome")    
# else:
#     print(f"The number {s} is not palindrome")  

    


# # 64.Wap to find the HCF of two numbers. 
# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))

# big=0
# small=0
# hcf=0

# if num1>num2:
#     big=num1
#     small=num2
# else:
#     big=num2
#     small=num1
  
    
# i=1
# while i<=small:
#     if num1 % i == 0 and num2 % i == 0:
#         hcf=i
#     i+=1 
# print("HCF is ",hcf)       
    

   
# 65.Wap to convert binary to decinaml. 
# bi = int(input("Enter binary number: "))
# temp = str(bi)

# isBinary = True
# i = 0

# # Validation
# while i < len(temp):
#     if temp[i] == "0" or temp[i] == "1":
#         i += 1
#     else:
#         isBinary = False
#         break
# # Conversion
# if isBinary:
#     decimal = 0
#     power = 0

#     while bi != 0:
#         ld = bi % 10
#         decimal += ld * (2 ** power)
#         power += 1
#         bi = bi // 10

#     print("Decimal number is", decimal)
# else:
#     print("Enter a valid binary number.")    
        
# # 66. Wap to convert decimal to binary. 
# decimal = int(input("Enter decimal number: "))
# binary=""
# while decimal!=0:
#     rem=decimal%2
#     binary=str(rem)+binary
#     decimal=decimal//2
# print("Binary no is ",binary)    



# 67.Wap to count the number of words in a string. 
#1way (without using split())
# str67="Hello    welcome   to our home!"
# count=0
# i=0
# while i<len(str67):
#     if str67[i]!=" ":
#         if i == 0 or str67[i-1] == " ":
#             count+=1
#     i+=1    
# print(count)        

#2way(with using split())
# str67 = "Hello    welcome   to our home!"

# words = str67.split()

# print("Number of words:", len(words))


# # 68.Wap to guess the number.
#1way 
# guess=int(input("enter the number:"))
# number=89
# attempts = 1

# while guess!=number:
#     if guess>number:
#         print("Too High! Try again")
#     else:
#         print("Too low! Try again")
        
#     attempts += 1    
#     guess=int(input("enter the number:"))
    
# print("Correct guess")
# print("Total attempts",attempts)    


#2way
# import random
# number = random.randint(1, 100)
# guess=int(input("enter the number:"))
# attempts = 1
# while guess!=number:
#     if guess>number:
#         print("Too High! Try again")
#     else:
#         print("Too low! Try again")
        
#     attempts += 1    
#     guess=int(input("enter the number:"))
    
# print("Correct guess")
# print("Total attempts",attempts)

 
# # 69.Wap to find the common elements in two sets 
# #1way
# set1 = {10, 20, 30, 40}
# set2 = {20, 30, 50, 60}

# lst1 = list(set1)
# common = set()

# i = 0
# while i < len(lst1):
#     if lst1[i] in set2:
#         common.add(lst1[i])
#     i += 1

# print(common)

# #2way
# set1={10,20,30,40}
# set2={20,30,50,60}
# common= set1.intersection(set2)
# print(common)


# 70.Wap to find the product of all the digits present in a number.
n=int(input("Enter nomber:"))
product=1
while n!=0:
    product*=n%10
    n=n//10
print("Product is",product)    



