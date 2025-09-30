# write a program using function to find greatest of three numbers.....

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
print(greatest(a,b,c))


# write a program using function to conert celsius to fahrenheit.....

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temprature in fahrenheit: "))
c = f_to_c(f)

print(f"{round(c, 2)} °C")


# how do you prevent a python print() function to print a new line at end.......

print("a")
print("b")
print("c", end="")
print("d")


# write a recursive function to calculate the sum of first n natural number....

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))