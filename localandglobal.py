#scope ----> talk about region 
#global-->we can access throw out code 
#local---> we can access only in the function

var1=10
def fun():
    var1=30#local has a high priority
    print(var1)#30
fun()
print(var1)#10

def fun():

    var2=30#local has a high priority
    print(var2)#30
fun()
# print(var2) #error that defined

var1=10
def fun():
    global var1
    var1=30#local has a high priority
    #another way 
    # globals()["var1"]=30---> we can also write like this 
    print(var1)#30
    
fun()     
print(var1)#10
  
#Decorators-->

def exampledec(fun):
    def wrap():
        print("no")
        print("no")
        fun()
        print("yes")
    return wrap

@exampledec
def printerz():
    print("hlo")
    
printerz()


set1={1,2,"ak",3,5,4,5,"akki"}
print(set1)
list1=list(set1)
print(type(list1))