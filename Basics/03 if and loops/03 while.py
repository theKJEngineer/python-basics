
number = 4

while number > 0:
    print(number)
    number = number -1

print("Kod po petli")




print()



number = 5

while number > 0:
    print(number)
    number = number - 1


print()



number = 1

while number < 6:
    print(number)
    number += 1


print()


num = 0
while True:                                             # pętla nieskonczona
    print("Wprowadz liczbe lub exit zeby zakonczyc")
    strData = input()
    if strData == "exit":
        break

    num = num + int(strData)                            # rzutowanie konieczne
    print("wartosc po dodaniu: " + str(num))            # rzutowanie konieczne






number = 3 

while number > 0:                                       # mozliwosc uzycia else z while, gdy warunek przestaje byc spelniany lub 
    print(number)                                       # nie był spełniony od poczatku
    number -= 1
else:
    print("Kod z else w petli while")





