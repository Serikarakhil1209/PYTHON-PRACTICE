#ways to run py
#1 IDLE OR CMD
#2 Notepad
#3 development platform (like vs or pycharm 0r........)



# DATA type 
#numeric-int,float,complex number ,boolen
#sequence-list , tuple,string,range
#set
#dictionary
#none


#int

num1=2
print(num1)


#float

num1=2.0
num2=2.0
print(num1+num2)

#complex number-> a+jn

a=5+3j
b=6-5j
print(a + b)
print(a * b)
print(a / b)
print(a ** b)
#print(a // b) #float division doesnot work on complext
#print(a % b)  # modules doest work on complex num

 

#Boolean is True or False

print(2>3) #False  0
print(2<=3) # True 1

bol=True
print(type(bol)) #boolean

#sequence

#list-> collection of element it may be anything

#***  list is 
# mutable 

list=[1,2,"AKki",True,[1,2,3]]
print(list)
print(list[4])
print(list[4][1])## nested list printing

print(list[-1:-6:-1])    #slicing also work on the list

list[1]="happy"
print(list)

#Tupel --> it is also a heterogenies but it is immutable

tuple1=(1,"ak",True,0.9,(1,2,3))
print(tuple1)
print(tuple1[4])
print(tuple1[4][1])## nested list printing
tuple1=("akhil")

print(tuple1)#reasign can be done on the tuple but not value change 

# we can not change  in the tuple 
# tuple is faster than list bcz in tuple only reading is allowed 


#range is nothing for generate the numbe range(0,100)
print(range(0,100))
print((range(0,100,2)))