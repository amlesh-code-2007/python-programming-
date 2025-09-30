''' 
    write a python function to print first n line of the following pattern:....
    *
    **
    ***
    ****
'''

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(6)


# write a python function which convert inches to cms.......

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"the corresponding value in cms is {inch_to_cms(n)}")


# write a python function to print multiplication table of a given number......

def multipliy(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multipliy(95)
