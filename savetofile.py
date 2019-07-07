with open("test.txt", "w") as open_file:
    open_file.write("druga vrstica\n")


with open("test.txt", "r") as read_file:
    vsebina = read_file.read()

print(vsebina)






f = open("test2.txt", "w")
f.write("kwkd\n")
f.close()