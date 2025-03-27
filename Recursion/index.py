# factorial
# num = 5
# def fact(num):
#     if num == 1 or num == 0:
#         return 1
#     result = num * fact(num-1)
    
#     return result
# print(fact(num))

#sum

# def sum_num(num):
#     if num == 0:
#         return 0
#     return num % 10 + sum_num(num // 10) 
# print(sum_num(12345))

#natural number

# def natural_number(num):
#     if num == 10:
#         return 10 
#     print(num)
#     return num + natural_number( num + 1 )
   
    
# natural_number(1)

#power
# def natural_number(num,power):
#     if power == 0:
#         return 1
#     return num * natural_number(num , power - 1)
   
# print(natural_number(5,10))


# def fib(n):
#     if n <=1:
#         return 1
#     print(n)
#     return fib(n-1) + fib(n-2)
# fib(20)

# def reverse_string(str):
#     temp = len(str)
#     if temp <= 0:
#         return 
#     return str(temp)
# print(reverse_string("akhil"))

list1=[1,2,3,4]
def rev_list(list1): 
    list2=[]
    if len(list1) <= 1:
        return list1
    return [list1[-1]] + rev_list(list1[ :len(list1)-1])

print(rev_list(list1))

