# # 111. Wap to get the following output. without length function. 
# #         S=’power star’ 
# #         Out={‘power’:5,’star’:4} 
# S="power star"
# out={}
# words=S.split()
# for i in words:
#     count=0
#     for ch in i:
#         count+=1
#     out[i]=count    
# print(out)    



# # 112. Wap to get the following output. 
# #         S=’power star’ 
# #         Out={‘power’:2,’star’:1}   (no of vowels is key) 
# S="power star"
# out={}
# words=S.split()
# for i in words:
#     vowels=0
#     for ch in i:
#         if ch in "aeiouAEIOU":
#             vowels+=1
#     out[i]=vowels    
# print(out) 
    



# # 113. Wap to get the following output. 
# #         S=’kabab is love’ 
# #         Out={‘kabab’:[‘babak’,2,’kbb’],’is’:[‘si’,1,’i’],’love’:[‘evol’,2,’lv’]} 
# #                         [reverse,no of vowels,char at even index] 
# S="kabab is love"
# out={}
# words=S.split()
# for i in words:
#     rev=""
#     vowels=0
#     evenIndex=""
#     for index,value in enumerate(i):
#         if value in "aeiouAEIOU":
#             vowels+=1
#         if index%2==0:
#             evenIndex+=value
             
#         rev=value+rev    
       
#     out[i]=[rev,vowels,evenIndex]        
# print(out)     



# # 114. Wap to get the following output. 
# #         S=’kabab is love’ 
# #         Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)} 
# #                     { 1st+last char:  (consonant,no of consonant,rev of consonant)} 
# S="kabab is love"
# out={}
# words=S.split()
# for i in words:
#     consonant=""
#     noConso=0
#     revConso=""
#     for ch in i:
#         if ch not in "aeiouAEIOU":
#             consonant+=ch
#             revConso=ch+ revConso
#             noConso+=1       
#     out[i[0]+i[-1]]=(consonant,noConso,revConso)  
# print(out)



# # 115.Wap to get the following output. 
# #         In=[100,200,35,40,60] 
# #         Out=[335,235,400,395,375] (total sum-value) 
# In=[100,200,35,40,60]
# out=[]
# total=0
# for i in In:
#     total+=i
# for i in In:
#     out.append(total-i)    

# print(out)     



    
# # 116. Wap to get the following output. 
# #             In=’bacbcaabbaa’ 
# #             Out=’b4a5c2’ 
# In="bacbcaabbaa"
# out=""
# temp={}
# for i in In:
#     if i not in temp:
#         temp[i]=1
#     else:
#         temp[i]+=1 
# for i in temp:
#     out+=i+str(temp[i])          
        
# print(out)           
        

          
        
        



# # 117. Wap to get the following output 
# #             In=[100,200,50,400,300] 
# #             N=300 
# #             Out=[[100,200],[300]] 
# In=[100,200,50,160,140,400,300] 
# target=300
# current_group = []
# current_sum = 0
# out = []

# for i in In:
#     current_group.append(i)
#     current_sum+=i
#     if current_sum==target:
#         out.append(current_group) 
#         current_sum=0
#         current_group=[]
#     elif current_sum>target:
#         current_sum=0
#         current_group=[]
    
# print(out)      
           
        
        
    



# # 118.Wap to check whether the number is strong or not. 
# n=int(input("enter number:"))
# temp=str(n)
# total=0
# for i in temp:
#     fact=1
#     for j in range(1,int(i)+1):
#             fact*=j
            
            
#     total+=fact       
# if total==n:
#     print("strong") 
# else:
#     print("not strong")           
        




# # 119.Wap to get the following output. 
# #             In={10:’star’,20:’bye’,30:’moon’,40:’apple’} 
# #             Out={10:’a’,20:’e’,30:’oo’,40:’ae’} 
#1way
# In={10:"star",20:"bye",30:"moon",40:"apple"}
# out={}
# for i in In:
#     store=""
#     for ch in In[i]:
#         if ch in "aeiouAEIOU":
#             store+=ch
#     out[i]=store       
# print(out) 



# #2way      
# In={10:"star",20:"bye",30:"moon",40:"apple"}
# out={}
# for key, value in In.items():
#     store = ""
#     for ch in value:
#         if ch in "aeiouAEIOU":
#             store += ch
#     out[key] = store
# print(out)




# 120. Wap to get the following output. 
#             In=[‘hello’,227,3.4,’last’,189,34] 
#             Out=[722,981,43] 
In=["hello",227,3.4,"last",189,34] 
out=[]
for i in In:
    if isinstance(i,int):
        rev=0
        while i!=0:
            ld=i%10
            rev=rev*10+ld
            i=i//10
        out.append(rev)      
print(out)      


