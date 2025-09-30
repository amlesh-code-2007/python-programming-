#  write a program to print multiplication table of given number...

n = int(input("Enter the number: "))

for i in range (1, 11):
    print(f"{n} x {i} = {n * i}")


# Attempt problem 1 using while loop....

m = int(input("Enter the number: "))

i = 1
while (i<11):
    print(f"{m} x {i} = {m * i}")
    i += 1


# write a program to print multiplication table of n using loop in reversed order.....

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n * (11-i)}")


# write a program to greet all the person names stored in list 'l' and which start with s.

l = ["Harry", "Shivam", "Shubham", "Sachin", "Aman", "Akash"]

for name in l:
    if(name.startswith("S")):
       print(f"Hello {name}")