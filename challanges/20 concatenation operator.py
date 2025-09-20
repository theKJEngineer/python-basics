
firstName = "Adam"
lastName = "Adam"

fullName= firstName + " " + lastName
print(fullName)


listOne = [1, 2, 3]
listTwo = [4, 5, 6]

combinedList = listOne + listTwo
print(combinedList)

if len(combinedList) > 5:
    print("lista jest dluga")
else:
    print("lista jest krotka")

greeting = "hello " + fullName

if "hello" in greeting:
    print(greeting)
