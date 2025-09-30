# write a code which work as catch the spam comment.....

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter the comment: ")

if((p1 in message) or (p2 in message) or (p3 in message)or (p4 in message)):
     print("this comment is spam")

else:
     print("print comment is not spam: ")


# write a program which find whether a username is contains less than 10 Character or not......

Username = input("Enter the username: ")

if(len(Username)>10):
     print("your username contain less than 10 character... ")

else:
     print("Your username contain more than 10 character... ")
  

# write a program which give me conformation wheather a given name is in list or not.....

l = ["Harry", "Shivam", "Shubham", "Akash"]

name = input("Enter your name: ")

if(name in l):
     print("Given name is inside the list: ")

else:
     print("Given name is not inside the list: ")