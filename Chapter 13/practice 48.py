from functools import reduce
# A list contains the Multiplication tables of 7. write a program to convert it to vertical string of same numbers....

table = [str(7*i) for i in range(1, 11)]

s = "\n".join(table)
print(s)


# write a program to find the maximum of the number in a list using the reduce function.........

l = [111, 2, 65, 675, 345, 982, 345, 46, 78]
print("In this list Highest number is: ")
def greater(a, b):
    if(a > b):
        return a 
    return b

print(reduce(greater, l))