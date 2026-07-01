# 71.Wap to print all the integers present in a list. 
# lst=[10,20,30,40,50,"avc",10.56]
# for i in lst:
#     # if type(i)==int:
#     if isinstance(i, int):
#      print(i)



# 72.Wap to find the length of homogenous tuple without len(). 
# tup1=(10,11,12,13,14,15)
# count=0
# for i in tup1:
#     count+=1
# print(count)    



# # 73.Wap to extract all the even numbers present in a list. 
# lst=[10,11,12,13,14,15,16,17]
# even_lst=[]
# for i in lst:
#     if i%2==0:
#         even_lst.append(i)
# print(even_lst)        


# # 74.Wap to remove duplicates from list  
# lst=[10,11,10,13,13,15]
# noDupli=[]
# for i in lst:
#     if i not in noDupli:
#         noDupli.append(i)
# print(noDupli)


# # 75.Wap to reverse a string without using slicing. 
# str1="Hello World"
# rev=""
# for i in str1:
#     rev=i+rev
# print("reverse is",rev)


# # 76.wap to extract all the lowercase characters in a string only if the ascii value is even.  
# str1="Hello World"
# out=""
# for i in str1:
#     # if "a" <= i <= "z" and ord(i)%2==0:
#     if i.islower() and ord(i) % 2 == 0:
#         out+=i
# print(out)



# # 77.Wap to check whether the last digit of an integer is even or not. 
#1way
# n=int(input("enter integer:"))
# if n%10 %2==0:
#     print("even")
# else:
#     print("odd")        

#2way
# n = int(input("Enter integer: "))
# temp = str(n)

# if int(temp[-1]) %2==0:
#     print("even")
# else:
#     print("odd") 


#3way(still using for)
# n = int(input("Enter integer: "))
# temp = str(n)

# for i in temp:
#     pass
# # After the loop finishes, i contains the last character.

# if int(i) % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
    
    
# #77.1. wap to replace space by underscore in string
# s="Python Java"
# res=""
# for i in s:
#     if i==" ":
#         res+="_"
#     else:
#         res+=i    
# print(res)    
  
  
  
# Range
# print(list(range(1,10,2)))  

# #for dictionary
# d={"a":1,"b":2}

# print(d.keys()) #[a,b]
# print(d.values()) #[1,2]
# print(d.items()) #[('a', 1), ('b', 2)]
# print(d["a"])  #1


# for i in d:  #here i in d is refers to keys
#     print(i, d[i]) #here d[i] refers to value





# #split(): convert string into list of string
# s = "Hello World"

# print(s.split()) #['Hello', 'World'] output is list
# print(s.split("o",1)) #['Hell', ' World']
# print(s.split("o",2)) #['Hell', ' W', 'rld']

# #strip()
# # It removes spaces from the beginning and end of a string.
# # It doesn't remove spaces in the middle.
# s = "    Hello World    "

# print(s.strip())
# price='$1000'
# print(price.strip("$"))


# #join(): list into string
# lst = ["Python", "Java", "SQL"]
# print(" ".join(lst)) #Python Java SQL




# # 78.Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers. 
# d = {"a": 10,
#     "b": 20,
#     1: 100,
#     "c": "Hello",
#     2: "Python",
#     "d": 40,
#     3.5: 50,
#     "e": 60
# }
# out={}
# for i in d:
#     if type(i)==str and type(d[i])==int:
#         # out.update({i:d[i]})
#         out[i]=d[i]
# print(out)

# # 79.Wap to extract key value pairs from the dictionary only if both keys and values are exactly same. 
# d = {"a": 10,
#     "b": "b",
#     1: 1,
#     "c": "Hello",
#     2: "Python",
#     "d": "d",
#     3.5: 3.5,
#     "e": 60
# }
# out={}
# for i in d:
#     if i==d[i]:
#         # out.update({i:d[i]})
#         out[i]=d[i]
# print(out)



# # 80.Wap to get the following output using len function. 
# #         S=’power star’ 
# #         Out={‘power’:5,’star’:4} 
# S="power star"
# out={}
# words=S.split()
# for i in words:
#     out.update({i:len(i)})
# print(out)    



# # 81.Wap to get the following output. 
# #         S=’power star’ 
# #         Out={‘power’:’rewop’,’star’:’rats’} 
# S='power star'
# out={}
# words=S.split()

# for i in words:
#     rev=""     # have to declare here if not it stores both for 2nd number {'power': 'rewop', 'star': 'ratsrewop'} Wrong op
#     for ch in i:
#         rev = ch + rev
#     out.update({i:rev})
# print(out)    



# # 82. wap to extract all the non default  values from a list. 
#1way
# lst=[10,20,0,0.0,"",{},99]
# out=[]
# for i in lst:
#     if i not in [0,0.0,(0j),False,"",[],(),set(),{}]:
#         out.append(i)
# print(out)        

#2way
# lst = [10,20,0,0.0,"",{},99]
# out = []
# for i in lst:
#     if i:
#         out.append(i)
# print(out)




# # 83.Wap to check whether the list is homogenous or not.
# lst=[10,20,9,30,40]
# firstType=type(lst[0])
# isHomogeneous = True
# for i in lst:
#     if type(i)!=firstType:
#         isHomogeneous = False
# if isHomogeneous:
#     print("list is Homogenous")       
# else:
#     print("list is hetrogenous")            


# # 84.Wap to replace the space by * present in a string 
# str1="Python Java"
# result=""
# for i in str1:
#     if i==" ":
#         result+="*"
#     else:
#         result+=i
# print(result)            


# # 85.Wap to count the number of occurrence of a specified character. 
# str1="Python Java and html"
# ch="a"
# count=0
# for i in str1:
#     if i==ch:
#         count+=1      
# print(count)


# # 86. Wap to get the following output. 
# #                 S=’always keep smiling’ 
# #                 Out-‘syawla peek gnilims’ 
# S="always keep smiling"
# words=S.split()
# out=""
# for i in words:
#     rev = ""
#     for ch in i:
#         rev = ch + rev
#     out+=rev+" "   
# print(out)    
       

# # 87. Wap to get the following output. 
# #                 In=’push maadi kushi padi’ 
# #                 Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’} 
# In="push maadi kushi padi"
# out={}
# words=In.split()
# for i in words:
#     store=""
#     if len(i)%2==0:
#         store=i[0]+i[-1]
#     else:
#         store=i[(len(i)//2)]   
#     # out.update({i:store})
#     out[i] = store       
# print(out)           



# # 88.Wap to toggle a string.
#1way (without built method)
# str1="Python Java"
# toggle=""

# for i in str1:
#     if "A"<= i <="Z":
#         toggle+=chr(ord(i)+32)
#     elif "a"<= i <="z":     
#         toggle+=chr(ord(i)-32)
#     else:
#         toggle+=i
# print(toggle)  


# #2way (with built method)
# str1="Python Java"
# toggle=""

# for i in str1:
#     if i.islower():
#         toggle+=i.upper()
#     elif i.isupper():     
#         toggle+=i.lower()
#     else:
#         toggle+=i
# print(toggle) 

          

# # 89.Wap extract upper, lower, digit and special characters present in a string to different output variable 
# #1way
# str1="Python %456 Java@123"
# up=""
# low=""
# digit=""
# special=""
# for i in str1:
#     if "A"<= i <="Z":
#         up+=i
#     elif "a"<= i <="z":     
#         low+=i
#     elif "0"<= i <="9":
#         digit+=i
#     else:
#         special+=i
# print(up)  
# print(low)
# print(digit)
# print(special)  


# #2way (built-in method)
# str1="Python %456 Java@123"
# up=""
# low=""
# digit=""
# special=""
# for i in str1:
#     if i.isupper():
#         up+=i
#     elif i.islower():     
#         low+=i
#     elif i.isdigit():
#         digit+=i
#     else:
#         special+=i
# print(up)  
# print(low)
# print(digit)
# print(special)


  
  # # 90. Wap to get the following output. 
# #             S=’hai hello ‘ 
# #             Out={‘hai’:’ai’,’hello:’eo’}
# S="hai hello"
# out={}
# words=S.split()
# # store=""
# for i in words:
#     # store=i[1]+i[-1]
#     #out.update({i:store}) 
#     # out[i]=store
#     out[i]=i[1]+i[-1] 
# print(out)      
 


# # 91. Wap to get the following output. 
# #             S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’] 
# #             Out=[‘com’,’py’,’html’,’org’] 
# S=["jiocinema.com","file.py","web.html","amazom.com","www.org"] 
# out=[]
# for i in S:
#     words=i.split(".")
#     if words[-1] not in out:
#         out.append(words[-1])
# print(out)     
    
    
       
# # 92. Wap to get the following output. 
# #             S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’] 
# #             Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], 
# #                 ’org’:[‘www’]} 
# S=["jiocinema.com","file.py","web.html","amazom.com","www.org","python.py"]
# out={}
# for i in S:
#     words=i.split(".")
#     if words[-1] not in out:
#         out[words[-1]]=[words[0]]
#     else:
#         out[words[-1]].append(words[0])   
           
# print(out)        




# # 93.Wap to get the following output. 
# #             L=[‘hai’,34,3.4,’hello’,90,’byebye’] 
# #             Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’} 
# L=["hai",34,3.4,"hello",90,"byebye"] 
# out={}
# for i in L:
#     # if type(i)==str:
#     if isinstance(i, str):
#         out[i]=i[0]+i[-1]
# print(out)


# # 94.wap to get the following output. 
# #             In=’hello’ 
# #             Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’} 
# In="hello"
# out={}
# for i in range(0,len(In)):
#  out[i]=In[i]

# print(out)


# # 95.Wap to extract all the string values present in list only if the string is palindrome. 
# #1way (slicing)
# lst=[10,20,"aba","abcd","xyx",99]
# res=[]
# for i in lst:
#     if isinstance(i,str) and i[::-1]==i:
#         res.append(i)
# print(res)        
        


#2way (without slicing)
# lst=[10,20,"aba","abcd","xyx",99]
# res=[]

# for i in lst:
    
#     if isinstance(i,str):
#         rev = ""
#         for ch in i:
#             rev = ch + rev

#         if rev == i:
#             res.append(i)   
# print(res)



# # 96.Wap to return the positions of vowels present in the given string.
# 1way
# str1="hello senorita!"

# for i in range(len(str1)):
#     if str1[i] in "AEIOUaeiou":
#         print(i,str1[i])
       
 
 
# #2way (using enumerate method ) 
# str1="hello senorita!"

# for index,value in enumerate(str1):
#     if value in "AEIOUaeiou":
#         print(index,value)



# # 97.Wap to check whether the given collection is having nested collection or not.
# lst1=[10,20,30,(10,20)]
# isNested = False
# for i in lst1:
#     # if type(i) in [list,tuple,set,dict]:
#     if isinstance(i, (list, tuple, set, dict)):
#         isNested=True
#         break
# if isNested:
#     print("Having nested collection")
# else:
#     print("no nested collection")            
        


 
# # 98.Wap to count the number of words in a string.
# str1="ai ml developer" 
# count=0
# words=str1.split()
# for i in words:
#     count+=1
# print(count)    
# # print(len(words))  #gives same output instead of using for loop




# 99.Wap to check whether the number is neon number or not. 
#             N=9→9**2=81→8+1=9 
#1way with string and for
# N=int(input("enter no"))
# square=N**2
# temp1=str(square)
# temp2=0
# for i in temp1:
#     temp2+=int(i)
   
# if N==temp2:
#     print("Neon number") 
# else:
#     print("No neon number")       



# #2way without string and using while
# N=int(input("enter no"))
# temp=N**2
# total=0
# while temp!=0:
#     ld=(temp%10)
#     total+=ld
#     temp=temp//10
# if N==total:
#     print("Neon number") 
# else:
#     print("No neon number")       
    




# # 100.Wap to find the longest word in a string. 
# str1="ai ml developer" 
# words=str1.split()
# long=words[0]
# for i in words:
#     if len(i)>len(long):
#         long=i
# print(long)        




# # 101.Wap to replace the special character present in a string by space. 
# str1="a#i m_l deve$loper" 
# out=""
# for i in str1:
#     # if i.isdigit() or i.islower() or i.isupper() or i==" ":
#     if i.isalnum() or i.isspace():
#         out+=i
#     else:
#         out+=" "    
# print(out)
    #isalpha() → Only letters
    # isdigit() → Only digits
    # isalnum() → Letters or digits
    # islower() → Lowercase letters
    # isupper() → Uppercase letters
    # isspace()



# # 102.wap to print the square of all the integers present in a list. 
# lst=[2,4,5,7.8,"ty"]
# for i in lst:
#     if isinstance(i,int):
#         print(f"square of {i} is {i**2}")



# # 103.Wap to extract all the odd number present at even index from a list. 
# lst=[10,20,33,57,56,74,89,91]
# out=[]
# for index,value in enumerate(lst):
#     if index%2==0 and value%2!=0:
#         out.append(value)
        
# print(out)




# # 104.Wap to extract all the mutable values present in a tuple. 
# t=(10,20,20.3,[89,34],"asd",(10+8j),(19,17),{},set())
# out=[]
# for i in t:
#     if isinstance(i,(list,set,dict)):
#         out.append(i)
# print(out)



# # 105.Wap to get the following output. 
# #             In=’10100011231’ 
# #             Out=’010111000’    ( 0→1 and 1→0 if it is other than 0 &1 ignore) 
# #1way
# In="10100011231"
# out=""
# for i in In:
#     if i=="0":
#         out+="1"
#     elif i=="1":
#         out+="0"
# print(out)            
    
        
# #2way
# In="10100011231"
# out=""
# for i in In:
#     if i not in "01":
#         continue
#     if i=="0":
#         out+="1"
#     elif i=="1":
#         out+="0"
# print(out)      



# # 106.Wap to get the following output. 
# #             In=’abacbaacc’ 
# #             Out={‘a’:4,’b’:2,’c’:3} 
#1way
# In="abacbaacc"
# out={}
# for i in In:
#     if i not in out:
#         out[i]=1
#     else:
#         out[i]+=1   
# print(out)


# #2ay (using out.get())
# In="abacbaacc"
# out={}
# for i in In:
#     out[i]=out.get(i,0)+1
# print(out)    
  
  
    
# # 107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype. 
# d = {
#     True: "Python",
#     False: "Java",
#     "a": 100,
#     10: "Hello",
#     20.5: "AI",
#     "b": 200,
#     (1, 2): "Tuple",
#     True: "Developer",
#     0:"ok"
# }
# out={}
# for i in d:
#     if isinstance(i, bool):
#         out[i]=d[i]
# print(out)        
        



# # 108.Wap to get the following output. 
# #                 In=’127342’ 
# #                 Out=’242173’  (extract even and odd digits separately and concatenate both) 
# In="127342"
# out=""
# even=""
# odd=""
# for i in In:
#     if int(i)%2==0:
#         even+=i      
#     else:
#         odd+=i   
# out=even+odd
# print(out)         
        




# # 109.Wap to checek whether the string is having only lowercase or not using continue. 
# str1 = "pythondeveEloper"
# isLower=True
# for i in str1:
#     if i.islower():
#         continue
#     else:
#         isLower=False
#         break
# if isLower:
#     print("Only lowercase")
# else:
#     print("Not only lowercase")        




# # 110.Wap to find the sum  square of individual digits of a string
# str1="asd1234l"
# total=0
# for i in str1:
#     if i.isdigit():      
#         total+=int(i)**2
# print(total)        
    

