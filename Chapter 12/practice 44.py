# write a list comprehences to print a list which contain the list multiplication table of a user entered number..

n = int(input("Enter a number: "))

table = [n*i for i in  range(1, 11)]
print(table)