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

