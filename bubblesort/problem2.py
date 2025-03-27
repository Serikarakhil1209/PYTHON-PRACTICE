# list1 = [20,15,26,2,98,6]
# list1 = list(set(list1))
# if len(list1) <=  1:
#     print("enter correct")    
# else:
#     for i in range(len(list1)-1):
#         for j in range(len(list1)-1):
#             if list1[j] > list1[j+1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]

# print(list1)
# print(list1[-2])
# print(list1[1])



# secound largest
# list1 = [20,15,26,2,98,6]
# first_max=float("-inf")
# secound_max=float("-inf")

# for i in list1:
#     if i > first_max:
#         first_max = i
# print(first_max)

# for i in list1:
#     if i > secound_max and i != first_max:
#         secound_max = i

# print(secound_max)

# minvalue

 
# list1 = [20,15,26,2,98,6]
# first_max=float("inf")
# secound_max=float("inf")

# for i in list1:
#     if i < first_max:
#         first_max = i
# print(first_max)

# for i in list1:
#     if i < secound_max and i != first_max:
#         secound_max = i

# print(secound_max)



# list1=[20,15,26,2,98,6]
# list2=[]

# for i in list1:
#     list2.append(i)
    
# list2.sort()


# index=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             index.append(j + 1)
# print(index)
            
        