# Write a program to calculate the grade of student from his marks from the following Scheme....

marks = int(input("Enter the marks obtained in 100: "))

if(marks<=100 and marks>90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("your grade is ", grade)


# write a program whether the given post talk about "Amlesh"...

post = input("Enter the post: ")

if("amlesh" in post.lower()):
    print("This post is talking about amlesh: ")

else:
    print("This post is not talking about amlesh: ")