import random

def game():
    print("Welcome to play")
    score = random.randint(1,66)

    with open(hiscore.txt) as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(score)
        else:
            hisocre = 0
        
    print(f"Your score: {score}")
    if(score>hiscore):
        with open("hiscore.txt", "w")as f:
            f.write(str(score))

    return score

game()