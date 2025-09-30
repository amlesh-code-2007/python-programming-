# write a program to find out whether a file is identical & matches the content of another file.....

with open("this.txt") as f:
    content1 = f.read()

with open("hello.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes these file are identical")

else:
    print("No these file is not matches")