#string--->
# string is immutable 

str="Akhil"  
print(str)

#SET--> unique,unorder and finite
#doesnt allow dupicate in the output it will not print the dupicate values


print("sets")
set1={2,3,2,3,0.8,2,4,2,4,5,6,True,0,8,"akki","str",2.0}

print(set1)


#Dictionary is key value pair 
#mutable and key should not be duplicate


print("dictionary")

dict1 ={
    1: "akhil",
    2:"akki" ,
    3:"akhil",
    "NAme":"Akki" ,
    3:"bhai" ,     #it will overide the value of three
    4:{
        1:"akki",
        2:2
        
    }
    
}
print(dict1)
print(dict1[3])
print(dict1[4])
print(dict1[4][1])

#None

str12=None
print(type(str12))
print(str12)
print(id(str12))


#Truthy values and Falsy valuesz
a=4+5j     
print(bool(a))



a=list(map(int, input().split(',')))

print(a)