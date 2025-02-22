#lamda----> lamda function is used for higher order functions like map , filter and reduc
#map
from Tools import reduce

def multiple(x):
    return x*-5
list1=list(map(multiple,[1,2,3,4,5,6]))
print(list1)

print(list(map(lambda x:x-5,[1,2,3,4,5,6])))

def multiple(x):
    return x%5==0
list1=list(map(multiple,[1,2,3,4,5,6]))
print(list1)### here it can give only true or false 


#filter

def multiple(x):
    return x%5==0
list1=list(filter(multiple,[1,2,3,4,5,6]))
print(list1) ##here it can give value 

list1=list(filter(lambda x: len(x) >= 5 , ["akki","akhil","mumma"]))
print(list1)

#reduce it will add multiply the total value five single value 

#we have to import reduce 
print(reduce(lambda x,y : x+y , [1,2,3,4,5,6]))

##issupersetv
  




