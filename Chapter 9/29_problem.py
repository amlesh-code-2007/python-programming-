# write a program to mine a log file and find out whether it contain 'python'

with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("yes, python is persent")

else:
    print("no, python is not persent")



# write a program to find out the line number where python is persent.....

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is persent. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No, python is not persent...")