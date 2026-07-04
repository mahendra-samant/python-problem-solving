#withoutA WithoutR
#Q)string conveert to uppercase
# def upper_case():
#     s=input("En ter a string:")
#     out=""
#     for i in s:
#         if i.islower():
#             out+=i.upper()
#         else:
#             out+=i
#     print(out)
# upper_case()                


#withA WithoutR
#Q)complex no from list
# def extractingC(ls):
#     compy=[]
#     for i in ls:
#         if isinstance(i,complex):
#             compy.append(i)
#     print(compy)
# ls=eval(input("Enter list:"))
# extractingC(ls)          


#withoutA WithR
# def fname():
#     a,b=10,20
#     return a+b,a-b,a*b
# res=fname()
# print(res,type(res))

#withA WithR
def fun(a,b):
    return a+b,a-b,a+b
a,b,c=fun(10,2)
print(a,b,c)