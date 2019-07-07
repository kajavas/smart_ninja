a = [1, 2, 3, 4, 5]
b = [1, "string", 1.23, [1, 2, 3]]

print(a)

print(a[0])
print(a[1])
print(a[-1])

print(b[-1])
print(b[-1][1])

print(b[1][2])


print(a[1:-1])
print(a[1:])
print(a[:-1])

print(a[1:4:2])

c = [2, 4, 1, 7, 8, 9, 3, 1]
c.sort()
print(c)


for el in c:
    print(el*10)

d = []
d.append("neka")

print(d)
d.append("vrednost")
d.append("3")

print(d)

#dolzina lista

print(len(d))






