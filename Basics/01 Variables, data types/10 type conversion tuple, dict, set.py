
listData = [1, 2, 3, 4, 5, 6]

tupleData = tuple(listData)                     # lista -> tuple
print(tupleData)

otherList = list(("Ola", 23, "Marek", 4365))
print(otherList)                                # tuple -> lista

setData = set(otherList)
print(type(setData))                            # list -> set
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))                      # tuple -> frozenset
print(frozenSetData)

tupleData = (("Ola", 1243),("Adam", 5467))      # 2x tuples w tuples bo musi byc para klucz-wartosci
dictData = dict(tupleData)                      # tuple -> dict
print(dictData)
print(dictData["Ola"])