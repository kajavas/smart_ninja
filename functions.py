def pozdrav():
    print("Pozdravljeni!")

pozdrav()

def boljsi_pozdrav(ime):
    print(f"Pozdravljen {ime}")

boljsi_pozdrav("Test")
boljsi_pozdrav("Kaja")
boljsi_pozdrav("Mirko")

def sestej(a, b):
    c = a + b
    return c

rezultat = sestej(3, 6)
print(rezultat)
print(sestej(5, 7))

print(pozdrav())

sestej(a=45, b=54)
sestej(b=43, a=76)
