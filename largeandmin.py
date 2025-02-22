# list1=[1,2,3,8,7,4]
# max_val=float('-inf')
# min_val=float('inf')
# for i in list1:
#     if i>max_val:
#         i,max_val=max_val,i
    
# list1=[2,3,8,7,4,1]
# max_val=list1[0]
# min=list1[0]
# sum=0
# for i in list1:
#     if i > max_val:
#         max_val=i
#     if i<min:
#         min=i
#     sum=sum+i
# print(max_val)
# print(min)
# print(sum)

# list2=[[2,3],[8,7,4]]
# sum=0
# for i in list2:
#     for j in i: 
#         sum=sum+j
# print(sum)

# list2=[[2,3],[8,7,4]]
# for i in list2:
#     sum=0
#     for j in i: 
#         sum=sum+j
#     print(sum)



factorial=0
def fact(num):
    for i in range(num):
        num=i*fact(num-1)
    return num
num=int(input())  
print(fact(num))    

 

        
