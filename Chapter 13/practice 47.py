# write a program to input name, marks and phone number of a student and format it using format function like below:

# "The name of the student is Amlesh, his marks are 84 and phone number is 9162123746"

name = input("Enter Name: ")
marks = int(input("Enter your Marks: "))
phone = int(input("Enter ur phone Number"))

s = "The name of the student is {}, his marks is {}, and phone number is {}".format(name, marks, phone)

print(s)