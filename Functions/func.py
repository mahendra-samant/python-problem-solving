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