d = {"kljuc": "vrednost",
     "janez": 13}

print(d)
print(d["janez"])

d[5] = "neka vrednost"

print(d)

print(len(d))

for key in d:
    print(key)
    print(d[key])

for key, value in d.items():
    print(key, value)


oseba = {"ime": "Matevz",
        "priimek": "Polensek",
        "leto_rojstva": 1985,
        "naslov": "Ulica 30"}

print(oseba.get("ime", -1))

