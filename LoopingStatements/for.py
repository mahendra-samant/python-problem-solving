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


  
# 90. Wap to get the following output.