# Write a program to filter a list of numnber which are divisible by 5.....

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 3, 45, 56, 450, 91, 985, 34525, 20, 43]
f = list(filter(divisible5, a))

print(f)