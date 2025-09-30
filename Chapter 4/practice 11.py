# Write a program to store six students results entired by users.....
Marks = []

m1 = int(input("Enter the student marks: "))
Marks.append(m1)
m2 = int(input("Enter the student marks: "))
Marks.append(m2)
m3 = int(input("Enter the student marks: "))
Marks.append(m3)
m4 = int(input("Enter the student marks: "))
Marks.append(m4)
m5 = int(input("Enter the student marks: "))
Marks.append(m5)
m6 = int(input("Enter the student marks: "))
Marks.append(m6)

Marks.sort()
print(Marks)

# write a program to count number is zeros in the tuple.....
s = (56, 89, 0, 56, 0, 100, 58, 98, 0)

n = s.count(0)
print(n)