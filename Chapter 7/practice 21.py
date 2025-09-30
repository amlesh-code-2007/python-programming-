# write a program to find given number is prime and not.....

n = int(input("Enter the number: "))

for i in range (2, n):
    if(n%i) == 0:
        print("Number is not prime: ")
        break
    else:
        print("Number is prime: ")
        break


# write a program to find the sum of first n number using whike loop....

n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)

# write a program to calculate the factorial of a given number using for loop.....

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")