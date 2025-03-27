# i=int(input("enter a number for 1 to 4"))
# if i >0 and i<=4:
#     dict= {
#     1:"jan",
#     2:"feb",
#     3:"march",
#     4:"april"
#     }
#     print(dict[i])
# else:
#     print("enter a correct in put")
    
# operation=input("").lower()
# op1=int(input())
# op2=int(input())

# if operation=="add":
#     print(op1+op2)
# elif operation=="sub":
#      print(op1+op2)
# elif operation=="mult":
#     print(op1+op2)
# elif operation=="div":
#     if op2 ==0:
#         print("you have enterd zero")
#     print(op1/op2)

# number=input()
# reverse=number[::-1]
# if number == reverse:
#     print("palindrome")
# else:
#     print("not p")

# number=int(input())
# digit=0

# while number>0:
#     digit=number%10
#     num1=digit*10+digit
#     number//10
#     if number == num1:
#         print("p")
#     else:
#         print("not p")

# teams = [1, 2, 3, 4, 6, 6]

# for i in range(len(teams)):  
#     if (i + 1) % 2 == 0:  
#         budget = teams[i] * 100
#         print(f"Team {i+1}: Budget is {budget}")
#     else:
#         print(f"Team {i+1}: Not allowed budget")

# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, number + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 break
#             else:
#                print(i)


# number = int(input("Enter a number: "))
# num = number
# add = 0

# string=len(str(number))

# while num > 0:
#     last_digit = num % 10
#     add += last_digit ** string
#     num //= 10

# if number == add:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# def amstrong(number):
#     add = 0
#     string=len(str(number))
#     temp = number
#     while number>0:
#         last_digit=number%10
#         add=add+last_digit**string
#         number//=10
#     if add == temp:
#         return True
#     else:
#         return False


# number1 = int(input("starting number"))
# number2 = int(input("enter end "))

# for i  in range(number1,number2):
#     if amstrong(i):
#         print(i)
    
# number1 = int(input("starting number"))
# number2 = int(input("enter end "))

# min=number1 if number1 < number2 else number2

# for i in range(1,min+1):
#     if number1 % i == 0 and number2 % i ==0:
#         print(i)


# def prime(number):
#     if number in [0,1]:
#         return False
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True

# num1=int(input("enter a number:"))

# temp=num1
# left_side_prime=0
# while True:
#     temp-=1
#     if temp<2:
#         break
#     else:     
#         if prime(temp):
#                left_side_prime=temp
#                break
        
# Right_side_prime=0
# while True:
#     temp+=1    
#     if prime(temp):
#          Right_side_prime=temp
#          break
# R_distance = Right_side_prime - num1
# l_distance = num1 - left_side_prime

# if l_distance == -1:
#     print(Right_side_prime)
# elif l_distance < R_distance:
#     print(left_side_prime)
# elif R_distance < l_distance:
#     print(Right_side_prime)
# else:
#     print(left_side_prime,Right_side_prime)


            
 