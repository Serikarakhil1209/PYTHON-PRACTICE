# list=["a","b","c","d","e"]
# for i in list:
#     print(i,end="")
    
# list=[2,3,5]
# sum=0

# for i in list:
#     for j in  range(2,i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print(sum)


# list1 = list(input(""))

# def list_find(list1):
#     sum=0
#     max=float('-inf')
#     min=float('inf')
#     for i in list1:
#         number=int(i)
#         sum+=number
        
#         if number > max:
#             max=number
    
#         if number<min:
#             min=number
    
        
#     return sum,max,min

# print(list_find(list1))


# Revese a list

# list1=[1,2,3,5,3,5,7,'true']
# temp=[]

# for i in list1:
#     temp.insert(0,i)
# print(temp)

#secound half reverse
# list1=[1,2,3,5,3,7]

# low=(len(list1)//2)
# high=len(list1)-1
# while high > low:
#     list1[low],list1[high]=list1[high],list1[low]
#     low+=1
#     high-=1
# print(list1)
    
# number1=list(input("enter a first list"))
# number2=list(input("enter a secound list"))

# flag=True
# def cheack_sub(num1,num2):
#     global flag
#     for i in num1:
#         if i not in num2:
#             flag=False
#             break  
#     return flag  

# cheack_sub(number1,number2)
        
# if flag == True:
#     print("number one is sub set of number 2")
# else:
#     print("not a ")


available_books = ["DSA", "Python", "C++", "Java", "ML"]
requested_books = ["DSA", "Python"]

# Output: "All requested books are available" ✅

# flag=True

# def cheack_book(books1,books2):
#     global flag
    
#     for i in books1:
#         if i not in available_books:
#             flag=False
#             break
#     return flag
# cheack_book(requested_books,available_books)
# if flag:
#     print("All requested books are available")
            

# all_books = ["DSA", "Python", "C++", "Java", "ML"]
# current_books = ["DSA", "Java", "ML"]

# missing_books=[]

# def cheack_book(all_books,current_books):
#     for i in all_books:
#         if i not in current_books:
#             missing_books.append(i)
#     return missing_books

# print(cheack_book(all_books,current_books))



borrowed_books = ["DSA", "Python", "Java", "Python", "ML", "Java", "Python"]


dict={
    
}
def most_borrowed(books):
    for i  in books:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict
most_borrowed(borrowed_books)
restult=max(dict,key.dict.get)
print(restult)

            
        
        
    



    
        

    