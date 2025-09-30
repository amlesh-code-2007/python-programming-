# write a game code in which we take input by user and contain in 'hi-score.txt' which is either blank or contain the previous hi-score..

import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 162)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

