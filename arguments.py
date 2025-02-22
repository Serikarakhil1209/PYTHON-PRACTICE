#arguments-positional,keyword,default 



#return statements- it will return value for us it return multiple values 

#multiple returns statments where print in tuple bcz we cant change

def find_great(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    print(hlo)#it will not print bcz it goes in dead state 
res=find_great(num1=1,num2=0)
print(res)


def find_great(num1,num2):
    return num1>num2 #it returns true 
res=find_great(num1=1,num2=0)
print(res)


# def multiple(num):
#     if num % 15==0:
#         return "fizz buzz"
#     elif num % 5==0:
#         return "buzz"
#     elif num % 3==0:
#         return " fizz"
    
#     return num
# # res=multiple(int(input()))
# # print(res)
#in python method overloading will not support so we will take arbitary argument
# def sum(a,b):
#     return a+b
# def sum(a,b,c):
#     return a+b+c
# def sum(a,b,c,d):
#     return a+b+c+d
 
# result=(sum(1,2))#error
# print(result)

# result=(sum(1,2,3))#error
# print(result)

# result=(sum(1,2,3,4))#it will print 
# print(result)

#arbitary argument

# def sum(a,b,*c):
#     return a+b+c
# def sum(a,b,c,d):
#     return a+b+c+d


def sum (*b):
    res =  0
    for i in b:
        res += i
    return res  





result=(sum(1,2,3))
print(result)

result=(sum(1,2,3,4))
print(result)
    



#keyword orbitary arguments
# eywords alsowe can pass k
def sum (**b):# all the be value goes in dectionary
    res =  0
    print(b)
    for i,j in b.items(): # j is value i is key
        res += j
    return res
        

result=(sum(num1=1,num2=2,num3=3))
print(result)

