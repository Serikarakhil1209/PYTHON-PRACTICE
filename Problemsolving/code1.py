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
    
operation=input("").lower()
op1=int(input())
op2=int(input())

if operation=="add":
    print(op1+op2)
elif operation=="sub":
     print(op1+op2)
elif operation=="mult":
    print(op1+op2)
elif operation=="div":
    if op2 ==0:
        print("you have enterd zero")
    print(op1/op2)
       