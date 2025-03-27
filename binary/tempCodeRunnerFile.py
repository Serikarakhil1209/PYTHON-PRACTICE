list1=[1,5,10,11,12,19,100,111]
list2=[4,5,-2,1]
output=[]
def binary(list1,list2):
    
    for i in list2:
        low=0
        high=len(list1)-1
        while low <= high:
            mid = (low+high) // 2
            if list1[mid] == i:
                output.append("true")
            elif list1[mid] > i:
                high = mid-1
            else:
                low = mid+1
        output.append("false")
    return output
print(binary(list1,list2))
