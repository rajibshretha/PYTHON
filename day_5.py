# function

a=int(input("Enter a number "))
b=int(input("Enter a number "))
def sum(a,b):
    print(a+b)
sum(a,b)

def goodday(name,end="GOODBYE"):#setting default value of end 
    print(f"Good morning {name} . {end}")
    
goodday("rajib")
goodday("raj","goodafternoon")

# Recursion

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
a=factorial(4)
print(a)


# p1
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in F : "))
print(f_to_c(f))


# p2

print("hello world",end="")
print("hello world",end="")

# p3

def sn(n):
    if(n==0 or n==1):
        return 1
    return (n+sn(n-1))
n=int(input("enter a number "))
print(sn(n))

# p4

# def pattern(n):
    if n==0:
        return
    print(f"{n*"*"}")
    pattern(n-1)

