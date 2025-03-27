# binary search algorith work on only sorted list

# list1=[-3,-2,1,2,3,4,6,7,8,15]
# search=-3


# def binnary_search(input_list,search):
#     low=0
#     high=len(input_list)-1
#     while low <= high:
        
#         mid=(low+high) // 2
        
#         if input_list[mid] == search:
#             return mid
#         elif input_list[mid] < search:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return "element not found"

# print(binnary_search(list1,search))


# list1=[1,1,2,3,5,6,7]

# def order(list1):
#     low=0
#     high=1
#     while high<len(list1):
#         if list1[low] <= list1[high]:
#             low+=1
            
#             high+=1
#             if high == len(list1):
#                 return "sorted"
#         else:
#             return "not in sorted"

# print(order(list1))

# list1=[8,7,6,5,4,3,2,7]


# def dec_order(list1):
#     left=0
#     right=1
#     while right<len(list1):
#         if list1[left] < list1[right]:
#             return "not"
#         left=left+1
#         right=right+1
#         return True
# print(dec_order(list1))


# list1=[1,5,10,11,12,19,100,111]
# list2=[4,5,-2,1]

# def binary(list1,list2):
#     output=[]    
#     for i in list2:
#         low=0
#         high=len(list1)-1
#         flag = False
#         while low <= high:
#             mid = (low+high) // 2
#             if list1[mid] == i:
#                 flag = True
#                 output.append("true")
#                 break
#             elif list1[mid] > i:
#                 high = mid-1
#             else:
#                 low = mid+1
#         if flag == False:
#              output.append("false")
#     return output
# print(binary(list1,list2))




# def cheack_repeate(number):
#     temp = number
#     list1=[]
#     while temp > 0:
#         last_num = temp % 10
        
#         if last_num in list1:
#             return "repeated"
#         else:
#             list1.append(last_num)
            
#         temp=temp // 10
#     return "not found"


# number=[123,233,345,768,111]
# output=[]

# for i in number:
#     output.append(cheack_repeate(i))
# print(output)
    
# finding the mising number
        
number=34571
# def finding_number(num):
#     temp=number
#     list1=[]
#     while temp > 0:
#         last=temp % 10
#         list1.append(last)
#         temp=temp // 10
#     return list1
# list2 = finding_number(number)
# output=[]
# min=min(list2)
# max=max(list2)
# for i in range(min,max+1):
#     if i not in list2:
#         output.append(i)
# print(output)



# prime number with missing number
    
# list1=[5,10,1,25,17,20]
# def find_missing_prime(list1):
#     min=1
#     max=25
#     new_list=[]
#     prime_list=[]

#     for i in range(min,max+1):
#         if i not in list1:
#             new_list.append(i)
    
#     for i in new_list:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             prime_list.append(i)           
#     return prime_list
                

# print(find_missing_prime(list1))

list1 = [568, 89, 112, 88, 571]

def increasing_order(list1):
    returning = []
    
    for num in list1: 
        
        temp = num  
        new_list1 = []  
        
        while temp > 0:
            last_val = temp % 10
            new_list1.append(last_val)
            temp = temp // 10  

        new_list1.reverse()  

        for i in range(len(new_list1) - 1):
            if new_list1[i] > new_list1[i + 1]:  
                returning.append("false")
                break
        else:
            returning.append("true")

    return returning

print(increasing_order(list1))
