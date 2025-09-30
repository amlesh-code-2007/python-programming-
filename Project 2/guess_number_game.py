# we are goning to write a program that generate a random number and asks the user to guess it.......

# if the player's guess higher than actual number, the program display "lower number please", similarly when guess is lower than actual number, 
    #   the program display "higher number please". when the user guesses is correct number, the program display the number
        #  of guesses the player used to arrive at the number......


import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 160. Try to guess it!")

n = random.randint(1, 160) 
a = -1
guesses = 0

while a != n :
    try:
      a = int(input("Guess the number: ")) 
      if(a > n):
          print("Too high! Try a lower number.")
          guesses +=1
      elif(a < n):
          print("Too low! Try a higher number")
          guesses +=1
    except ValueError:
        print("❌ Please enter a valid number.")

print(f"🎉 Congratulations! You guessed the number {n} correctly in {guesses} attempts.")