# Create an empty dictionary and allow to insert 4 friend ours names and language assume their names are unique....

d = {}
name = input("Enter the name: ")
lang = input("Enter the lang: ")
d.update({name: lang})
name = input("Enter the name: ")
lang = input("Enter the lang: ")
d.update({name: lang})
name = input("Enter the name: ")
lang = input("Enter the lang: ")
d.update({name: lang})
name = input("Enter the name: ")
lang = input("Enter the lang: ")
d.update({name: lang})

print(d)

# write a program in which we write 18(int), '18'(str)as a value of it...

s = set()
s.add(18)
s.add('18')

print(s)

# what will the lenght of the following set....

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s))