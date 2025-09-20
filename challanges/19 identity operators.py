
text = "hello"
print(dir(text))
print(text.upper())

x = 256
y = 256

print(x is y)

listOne = [1, 2, 3]
listTwo = listOne

print(listOne is listTwo)

listOne.append(10)

if 10 in listTwo:
    print("10 dodało sie tez do listy B")

listThree = [1, 2, 3, 10]

if listOne is listThree:
    print("listy sa takie same")
else:
    print("listy sa rozne")