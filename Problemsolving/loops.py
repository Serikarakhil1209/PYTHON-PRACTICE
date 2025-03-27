# # task1

# for i in range(1,101):
#     print(i)

# #task2

# n=5
# sum=(n*(n+2))/2
# print(sum)


# #task3

# num=1
# while(num<=50):
#     print(num)
#     num+=1
    
# #task4


# number=int(input("enter a number "))

# for i in range(1,11):
#     print(number ,"*" ,i ,"=", i*number)
    

#task5  important  reversing number and finding sum

# number=int(input(""))

# rev_number=0
# sum1=0

# while(number>0):
#     rem= number % 10
#     number=number // 10
#     rev_number=rev_number*10+rem
#     sum1=sum1+rem
# print(rev_number)
# print(sum1)

#count number digit
 
# number=123
# count=0
# while(number>0):
#    number = number // 10
#    count +=1
# print(count)


# number=1
# while(number!=0):
#     if number > 0:
#         number=int(input("enter again"))
#     else:
#         print("you are exit now")
#         break
    

# number=1
# while(number!=0):
#     number=int(input("enter again"))
    
   
#medium

#3

# num=5
# fact=1
# i=1

# while i <= num:
#     fact*=i
#     i+=1
# print(fact)





# number=int(input("enter a fibonacci"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(number):
#     c=a+b
#     a=b
#     b=c
#     print(c)    

#task 4

# for i in range(101):
#     if i % 3 ==0 and i % 5 ==0:
#         print(i)

# pass1=input("enter a password")
# passowd="abc"
# count=0
# while(count<3):
#     if pass1 == passowd :
#         print("login")
#         break
#     else:
#         pass1=input("retry")
#         count+=1

#prime number

# number=int(input("enter a num"))
# count=0
# for i in range(1,number+1):
#     if number % i == 0:
#         count+=1
# if count == 2:
    
#     print("it is a prime")
# else:
#     print("it is not a prime ")

##case 1


# number=int(input("enter a num"))
# spy=False
# if number in [0,1]:
#    print("not a prime") 
# else: 
#    for i in range(2,number):
#        if number % i == 0 :
#            spy=True
#            print("not a prime ")
#            break
#    if spy == False:
#        print("prime")

#case 2

# number=int(input("enter a num"))
# spy=False
# if number in [0,1]:
#    print("not a prime") 
# else: 
#    for i in range(2,( number // 2)+1):
#        if number % i == 0 :
#            spy=True
#            print("not a prime ")
#            break
#    if spy == False:
#        print("prime")


# number=int(input("enter a num"))
# spy=False
# if number in [0,1]:
#    print("not a prime") 
# else: 
#    for i in range(2,int(number ** 0.5)+1):
#        if number % i == 0 :
#            spy=True
#            print("not a prime ")
#            break
#    if spy == False:
#        print("prime")


while True:
    number=int(input("type 1 for square  or type 2 for cube or 3 for exit"))
    if number == 1:
       num1=float(input("enter number for square "))
       square=num1**2
       print("square :" , square)
    elif number == 2 :
       num1=float(
                  ("enter number for cube3 "))
       cube=num1**3
       print("cube:",cube)
    elif number == 3:
        break
    else:
        print("invalid option")
       
       
       




