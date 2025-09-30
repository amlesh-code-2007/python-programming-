# Count how many vowels (a, e, i, o, u) are in the given string......

def count_vowel(s):
    Vowels = "a,e,i,o,u,A,E,I,O,U"
    count = 0
    for char in s:
        if char in Vowels:
            count += 1
    return count
    
text = input("Enter the text: ")

vowel_count = count_vowel(text)

print(f"Number of vowels in the string: {vowel_count}")