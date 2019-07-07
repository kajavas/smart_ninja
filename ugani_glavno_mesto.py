import random


def choose_random_country(country_dict):
    drzave = country_dict.keys()
    return random.choice(list(drzave))


def check_guess(country_dict, selected_country, user_guess):
    return user_guess == country_dict[selected_country]


#drzave = drzava_mesto.keys()
#izbrana_drzava = random.choice(list(drzave))
#print(izbrana_drzava)

drzava_mesto = {"Slovenija": "Ljubljana",
                "Avstrija": "Dunaj",
                "Anglija": "London"}

chosen_country = choose_random_country(drzava_mesto)

print(f"What is the capital of {chosen_country}?")
for guess_num in range(5):
    ans = input("ANS: ").lower().capitalize()
    if check_guess(drzava_mesto, chosen_country, ans):
        print("Bravo!")
        break
    print("Noup... Try again...")



