# write a code to find the simple interest value
# give the value of amount
Principle = float(input("How many u give in simple interst?\n"))

# give the value of time
time = float(input("how many years after he will give u money?\n"))

# give the value of rate
rate = float(input("how much interest u can put in ur amount?\n"))

# calculated it all
simple_interest = (Principle * time * rate) /100

# print the value
print("simple interest =", simple_interest)
