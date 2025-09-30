# write a program to read the text from a given file 'poems.txt' and find out wheather it contain the word 'twinkel'

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()