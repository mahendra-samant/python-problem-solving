# # 121.Wap to check whether the number is strong or not. 
# def strong_Number(num):
#     temp=str(num)
#     total=0
#     for i in temp:
#         fact=1
#         for j in range(1,int(i)+1):
#             fact*=j
            
#         total+=fact    
#     if total==num:
#         return "strong Number"
#     else:
#         return "Not Strong Number" 
        
# result=strong_Number(145)        
# print(result)


# # 122.Wap to print the strong numbers between the given range. 
# def strongInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
    
#     if sNum<eNum:
#         for i in range(sNum,eNum):
#             temp=str(i)
#             total=0
#             for s in temp:
#                 fact=1
#                 for j in range(1,int(s)+1):
#                     fact*=j
                    
#                 total+=fact    
#             if total==i:
#                 print(i)
           
#     else:
#         print("Invalid Range")            
# strongInRange()  
            
    


# # 123.Wap to find the nth strong number. 
# def nStorngNumber(num):
    
#     count=0
#     current=1
#     while True:
#         temp=str(current)
#         total=0
#         for i in temp:
#             fact=1
#             for j in range(1,int(i)+1):
#                 fact*=j
                
#             total+=fact    
#         if total==current:
#             count+=1
#             if count==num:
#                 return f"{num}th strong number is {current}"
            
#         current+=1  
                   
# result=nStorngNumber(4)        
# print(result)




# # 124.Wap to check whether the number is arm strong or not. 
# def armstrongNo(num):
#     temp=str(num)
#     total=0
#     count=0
#     #count = len(temp)   this is better as we dont need of extra for loop.......
#     for i in temp:
#         count+=1
#     while num!=0:
#         ld=num%10
#         total+=(ld**count)
#         num=num//10
#     if total==int(temp):
#         return f"{int(temp)} is Armstrong number"  
#     else:
#         return f"{int(temp)} is not Armstrong number"  
            
# result=armstrongNo(153)
# print(result)




# # 125.Wap to print the arm strong numbers between the given range. 
# def armstrongInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for i in range(sNum,eNum):
#             temp=str(i)
#             num=i
#             total=0
#             count=0
#             #count = len(temp)   this is better as we dont need of extra for loop.......
#             for j in temp:
#                 count+=1
#             while num!=0:
#                 ld=num%10
#                 total+=(ld**count)
#                 num=num//10
#             if total==i:
#                 print(f"{int(temp)} is Armstrong number") #dont return the value here as we are printing the values betwwen ranges  
#     else:
#         print("Invalid Range")    

# armstrongInRange()




# # 126.Wap to find the nth arm strong number. 
# def nArmStorngNumber(num):

#     current=1
#     found=0
#     while True:       
#         temp_num=current
#         total=0
#         count_digit = len(str(current))  # this is better as we dont need of extra for loop.......
        
#         while temp_num!=0:
#             ld=temp_num%10
#             total+=(ld**count_digit)
#             temp_num=temp_num//10
            
#         if total==current:
#             found+=1
#             if found==num:
#                 return f"{num}th Armstrong number is {current}"
            
#         current+=1  
                   
# result=nArmStorngNumber(10)  
# print(result)



# # 127.Wap to check whether the number is perfect or not. 
# def perfectNo(num):
#     total=0
#     i=1
#     while i<num:
#         if num%i==0:
#             total+=i
#         i+=1
#     if total==num:
#         return f"The number {num} is perfect"
#     else:
#         return f"The number {num} is not perfect"        
    
# result=perfectNo(28)
# print(result)



# # 128.wap to print the perfect numbers between the given range. 
# def perfectNoInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for j in range(sNum,eNum):
#             total=0
#             i=1
#             while i<j:
#                 if j%i==0:
#                     total+=i
#                 i+=1
#             if total==j:
#                 print(f"The number {j} is perfect")        
       
#     else:    
#         print("Invalid Range")

# perfectNoInRange()



# # 129.Wap to find the nth perfect number. 
# def nperfectNo(num):

#     current=2
#     found=0
#     while True:       
#         total=0
#         i=1
#         while i<current:
#             if current%i==0:
#                     total+=i
#             i+=1
           
            
#         if total==current:
#             found+=1
#             if found==num:
#                 return f"{num}th perfect number is {current}"
            
#         current+=1  
                   
# result=nperfectNo(3)  
# print(result)



# 130.Wap to check whether the number is prime or not. 
# def primeNo(num):
#     isPrime=True
#     i=2
#     if num>1:
#         while i<num:
#             if num % i == 0: 
#                 isPrime=False
#             i+=1
            
#         if isPrime==True:
#             return f"{num} is prime number"
#         else:
#             return f"{num} is not prime number"
#     else:
#         return f"{num} is not a prime number"        
                
    
# result=primeNo(12)
# print(result)



# # 131.wap to print the prime numbers between the given range. 
# def primeNoInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for j in range(sNum,eNum):
#             isPrime=True
#             i=2
#             if j>1:
#                 while i<j:
#                     if j % i == 0: 
#                         isPrime=False
#                     i+=1
                    
#                 if isPrime==True:
#                     print(f"{j} is prime number")
                      
#     else:    
#         print("Invalid Range")

# primeNoInRange()




# # 132.Wap to find the nth prime number. 
# def nprimeNo(num):

#     current=2
#     found=0
#     while True:       
#         isPrime=True
#         i=2
#         while i<current:
#                 if current % i == 0: 
#                     isPrime=False
#                 i+=1
           
            
#         if isPrime==True:
#             found+=1
#             if found==num:
#                 return f"{num}th prime number is {current}"
            
#         current+=1  
                   
# result=nprimeNo(6)  
# print(result)



# # 133.Wap to check whether the number is Fibonacci number or not. 
# def fibonacciNo(num):
#     if num == 0:
#         return f"{num} is Fibonacci number"
#     a=0
#     b=1
#     while b<=num:
#         if b==num:
#             return f"{num} is Fibonacci number"
#         c=a+b
#         a=b
#         b=c
               
#     return f"{num} is not Fibonacci number"      
# result=fibonacciNo(0)
# print(result)




# # 134.wap to print the Fibonacci numbers between the given range. 
# def fibonacciNoInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for j in range(sNum,eNum):
#             if j == 0:
#                 print(f"{j} is Fibonacci number")
#                 continue  #when we use continue so after chekinj j==0 it will not gone check in while loop condition it will start from 1
#             a=0
#             b=1
#             while b<=j:
#                 if b==j:
#                     print(f"{j} is Fibonacci number")
#                     break   #it it used to handle duplicate, that is 0,1,1,5,8 (1 is repeating)
#                 c=a+b
#                 a=b
#                 b=c
                
                       
#     else:    
#         print("Invalid Range")

# fibonacciNoInRange()



# # 135.Wap to find the nth Fibonacci number. 
# def nfibonacciNo(num):
#     if num <= 0:
#         return "Invalid position"
#     a=0
#     b=1
#     count=1
#     while count<num:
#         c=a+b
#         a=b
#         b=c
#         count+=1
#     return f"{num}th Fibonacci number is {b}"    
                   
# result=nfibonacciNo(6)  
# print(result)


# # 136.Wap to check whether the number is palindrome or not. 
#1way
# def palindromeNo(num):
#     temp=str(num)
#     if num==int(temp[::-1]):
#         return f"{num} is palindrome number"
#     else:
#         return f"{num} is not palindrome number"
    
# result=palindromeNo(121)
# print(result)


#2way
# def palindromeNo(num):
#     temp=num
#     rev=0
#     while num!=0:
#         ld=num%10
#         rev=rev*10+ld
#         num=num//10
#     if rev==temp:
#         return f"{temp} is palindrome number"
#     else:
#         return f"{temp} is not palindrome number"  

# result=palindromeNo(122)
# print(result)



# # 137.wap to print the palindrome numbers between the given range. 
# def palindromeNoInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for j in range(sNum,eNum):
#             temp=str(j)
#             if j==int(temp[::-1]):
#                 print(f"{j} is palindrome number")

#     else:    
#         print("Invalid Range")

# palindromeNoInRange()



# # 138.Wap to find the nth palindrome number. 
# def npalindromeNo(num):
#     if num>0:  # if the palindrome start form 1 
#         count=0
#         current=1 # if the palindrome start form 1 otherwise if starts from 0 then current=0
        
#         while True:
#             temp=str(current)
#             if current==int(temp[::-1]):
#                 count+=1
#                 if count==num:
#                     return f"{num}th palindrome number is {current}"
#             current+=1
        
#     else:
#         return "Invalid input"   
    
# result=npalindromeNo(16)  
# print(result)



# # 139.Wap to check whether the number is happy number or not. 
# def happyNo(num):
#     seen=set()
#     temp=num
#     while num !=1:
#        if num in seen:
#            return f"{temp} is Not Happy number"
#        seen.add(num)
#        total=0
#        while num!=0:
#            total+=((num%10)**2)
#            num=num//10
#        num=total  
    
#     return f"{temp} is  Happy number"     
           

# result=happyNo(7)
# print(result)   


# # 140.wap to print the happy numbers between the given range. 
# def happyNoInRange():
#     sNum=int(input("Enter starting num:"))
#     eNum=int(input("Enter ending number:"))
#     if sNum<eNum:
#         for j in range(sNum,eNum):
#             seen=set()
#             num=j
#             temp=num
#             while num !=1:
#                 if num in seen:
#                     break
#                 seen.add(num)
#                 total=0
#                 while num!=0:
#                     total+=((num%10)**2)
#                     num=num//10
#                 num=total  
#             if num == 1:
#                 print(f"{temp} is  Happy number")
            
    
#     else:    
#         print("Invalid Range")

# happyNoInRange()


# # 141.Wap to find the nth happy number. 
# def nhappyNo(num):
    
#     current=1
#     found=0
#     while True:
#         seen=set()
#         original=current
        
#         while current !=1:
#             if current in seen:
#                 break
#             seen.add(current)
            
#             temp_num=current
            
#             total=0
#             while temp_num!=0:
#                 total+=((temp_num%10)**2)
#                 temp_num=temp_num//10
#             current=total  
        
#         if current == 1:
#             found+=1
#             if num==found:
#                 return f"{num}th Happy number is {original}"
    
#         current = original + 1
        
# result=nhappyNo(3)
# print(result)    
