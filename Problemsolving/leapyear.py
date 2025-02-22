# year =int(input("enter a year"))

# if (year % 4 == 0 and year % 100 !=0) or (year % 400==0):
#     print("it is a leap year")
# else:
#     print("it is not a leap year")
    

# side1=int(input("enter a side1"))
# side2=int(input("enter a side2"))
# side3=int(input("enter a side3"))
# if side1+side2 > side3 or side2+side3 > side1 or side3+side1 > side2:
#     print("it is tri")
# else:
#     print("not a tri")

# scoore=int(input("enter a scoore:"))

# if scoore>=90:
#     print("A")
# elif scoore>=80:
#     print("B")
# elif scoore>=70:
#     print("c")
# else:
#     print("CM")



charcter=input("").lower()
list1=["a","e","i","o","u"]


if charcter in list1:
    print("vowel")
elif charcter.isalpha():
    print("const")
else:
    print("neither")
