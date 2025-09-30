# A file contains a word 'donkey' multiple times you need. to write a programme which replaced this word with ##### by updating the sample file 

word = "donkey"

with open("file.txt") as f:
    contain = f.read()

containNew = contain.replace(word, "#####")

with open("file.txt", "w") as f:
    f.write(containNew)


# Repeat programm 4 for a list of such words to be censored
words = ["donkey", "king", "animals"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)