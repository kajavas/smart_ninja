import random
import json

score_file_name = "score.txt"

player_name = input("Enter your name: ")

with open("score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list = sorted(score_list, key=lambda k: k ["score"])
    print(f"Najboljsi trije igralci: {score_list[:3]}")


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
        score_list.append(
            {"name": player_name,
             "score": loop+1}
        )
        with open(score_file_name, "w") as score_file:
            score_file.write(json.dumps(score_list))
        break



