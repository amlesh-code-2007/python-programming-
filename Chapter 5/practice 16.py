# Create a dictionary with 3 fruits and their colors. Print the dictionary..............
fruit = {
    "apple": "red",
    "banana": "Yellow",
    "Grape": "Purpule"
}

print(fruit)


# Original dictionary.....
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

del fruits["grape"]
print(fruits)


#Add a new key-value pair to an existing dictionary...
dic = {
    "apple": "red",
    "banana": "yellow",
}

fruit = input("Enter the fruit: ")
colour = input("Enter the colour: ")
dic.update({fruit: colour})
print(dic)


# Access the value using a key.......
Fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

print("Colour of banana is: ", Fruits["banana"])