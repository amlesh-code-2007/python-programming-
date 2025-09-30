# write a program in which user input name but show after good morning....

name = input("Enter the name of user: ")

print(f"Good Morning {name}")

# fill in letter templet given below.....

letter = ''' 
Dear <|Name|>,
           you are Selected!
<|Date|>
           '''

print(letter.replace("<|Name|>", "Amlesh").replace("<|Date|>","30 september 2050"))

# write a program to format using escape sqeuence letter.......

letter = "Dear Amlesh,\n\t This python course is nice.\nThanks"
print(letter)

# write a program to replace a extra space in the string....
frame = "Dear Amlesh ur unlucky person   in the planets.."

print(frame.find("  "))
print(frame.replace("  ",""))