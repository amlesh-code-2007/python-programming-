# write a program to find out wheather a student has passed or failed if it's required 40% and at least 33% in an subject to pass. Assume five subjects and take marks as input from the user..

Marks1 = int(input("Enter the marks1: "))
Marks2 = int(input("Enter the marks2: "))
Marks3 = int(input("Enter the marks3: "))
Marks4 = int(input("Enter the marks4: "))
Marks5 = int(input("Enter the marks5: "))

total_percentage = (100*(Marks1+Marks2+Marks3+Marks4+Marks5))/500

if(total_percentage>=40 and Marks1>=28 and Marks2>=28 and Marks3>=28 and Marks4>=28 and Marks5>=28):
    print("you are passed:", total_percentage)

else:
   print("you failed, try again next year!", total_percentage)


# write a program to find the greatest of four number entered by user........

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("Greatest number is n1:", n1)

elif(n2>n1 and n2>n3 and n2>n4):
    print("Greatest number is n2:", n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print("Greatest number is n3:", n3)

elif(n4>n1 and n4>n2 and n4>n3):
    print("Greatest number is n4:", n4)