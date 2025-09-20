
numbers = [7, 8, 9, 10, 11, 12]
print(numbers)

tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["ABC", 233, 435.4333, "XYZ"]
print(mixedList)

setMixed = set(mixedList)
print(setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers))
print(frozenSetNumbers)

nameAgeParis = (("Adam", 23), ("Ola", 54), ("Ala", 66))
ageDict = dict(nameAgeParis)
print(ageDict)
print(ageDict["Adam"])
