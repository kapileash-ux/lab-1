'''
#task 1
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>=b and a>=c:
    print("a is a largest number")
elif b>=a and b>=c:
    print("b is a largest number")
else:
    print("c is the largest number")

#task 2
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a<=b and a<=c:
    print("a is a smallest number")
elif b<=a and b<=c:
    print("b is a smallest number")
else:
    print("c is the smallest number")

#task 3
a=int(input("enter a number:"))
if a>0:
    print("it is positive")
elif a<0:
    print("its is negative")
elif a==0:
    print("zero")

#task 4
a=int(input("enter no.of days:"))
if a>0 and a<=5:
    print(a*0.40)
elif a<=6 and a<=10:
    print(a*0.65)
else:
    print(a*0.80)

#task 5
a=float(input("enter a number:"))
b=float(input("enter a number:"))
operation=input("enter the operation:")
if operation=="+" :
    print(a+b)
elif operation=="-" :
    print(a-b)
elif operation=="*" :
    print(a*b)
elif operation=="/":
    print(a/b)
    
#TASK 6
n=int(input("enter a number:"))
if n%5==0:
    print("multiple of 5")
elif n%3==0:
    print("multiple of 3")
elif n%7==0:
    print("multiple of 7")
else:
    print("not multiple of 5,3 and 7")
'''
#task 7
# task 7
w = int(input("enter the weight:"))
t = input("enter the type of booking:")

if w <= 100:
    if t == "o":
        print("80")
    else:
        print("100")

elif w <= 500:
    if t == "o":
        print("150")
    else:
        print("200")

elif w <= 1000:
    if t == "o":
        print("210")
    else:
        print("250")

else:
    if t == "o":
        print("250")
    else:
        print("300")
