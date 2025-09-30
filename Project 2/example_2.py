# Write a function that checks if a string is a palindrome or not....

def is_palindrome(s):
    s = s.replace(" ","").lower()

    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("It is a palindrome: ")

else:
    print("It is not palindrome: ")
