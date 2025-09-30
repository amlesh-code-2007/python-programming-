# write a program to make a copy of a text file "this.txt"

with open("this.txt") as f:
    content = f.read()

with open("", "w") as f:
    f.write(content)
