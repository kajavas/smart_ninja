#del, ko sem manjkala 24.6.

import random

score_file_name = "score.txt"
try:
    with open(score_file_name, "r") as score_file:
        old_score = int(score_file.read())
except (FileNotFoundError, ValueError):
    old_score = 1000

secret_num = random.randint(0,100)

for loop in range(10):
    guess = int(input("Guess secret number between 0 and 100: "))

    if secret_num > guess:
        print("Ugibaj visje...")
    elif secret_num < guess:
        print("Ugibaj nizje")
    else:
        print("Uganil si!")
        if old_score > loop:
            with open(score_file_name, "w") as score_file:
                score_file.write(str(loop+1))
        break