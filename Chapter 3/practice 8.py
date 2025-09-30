# use of string in diffrent ways.......
name ="Amlesh"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[4]
print(character1)

print(name[:4]) # is same as print(name[0:4])
print(name[2:]) # is same as print(name[2:5])

print(name[-4:-1]) # is a negative in inilization index...
print(name[2:5]) # it's a transpose of negative inilization index...

print(len(name))
print(name.endswith("esh"))
print(name.startswith("am"))
print(name.capitalize())

a = "I am good boy but\nit\'s depend on ur behaviour\n"

print(a)