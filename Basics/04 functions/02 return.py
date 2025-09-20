

def addNumbers(a,b,c):
    return a + b + c

def sumListsElements(listData):
    if len(listData) == 0:
        print("Pusta lista")
        return None                     # return powoduje wyjscie z funkcji
    result = 0
    for i in listData:
        result = result + i
    return result

print(sumListsElements([]))
print(sumListsElements([1,2,3,4,5,6]))



# return jest nie obowiazkowe jesli funkcja nie zwraca konkretnej wartosci:

def printList(listData):
    if len(listData) == 0:
        return
    for i in listData:
        print(i)            # bez return działą tak samo jak z 


printList([])               # pusta lista, brak informacji w terminalu
printList([6,7,8])

