
# practice set of python
# 1
a = 10
b = 30
if a>b:
    print("A is greater than B")

else:
    print("B is greater than A")    


# # 2 check the gender and print hello sir and hello  maa'm
c = str(input("Enter your Gender: "))

if c=="male" or c=="M":
    print("Hello sir good morning: ")
elif c=="Female":
    print("Hello maam good morning: ")

else:
    print("Hello sir: ")    

# 3 check odd Or not even

number=int(input("Enter a number:= "))
if number//2:
    print("this is even number")

else:
    print("This is a odd number")    



 # (4) check the student are eligible for vote  :

num =int(input("Enter your age = "))
if num>18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")


# (5) check the leap year not not...

year = int(input("Enter years = "))
if year%100==0 or year%400==0:
    print("THis is a leap years")

elif year%100!=0 or year%400==0:
    print("this is leap years")

else:
    print("this is  years")    