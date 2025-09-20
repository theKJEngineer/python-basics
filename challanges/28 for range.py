
# zad 1:

sum = 0
for i in range(201):
    sum = sum + i
    
print (sum)



sum = 0
for i in range(50,101):
    sum = sum + i

print(sum)




sum = 0
for i in range(0, 300, 3):
    sum = sum + i

print(sum)
print()


# zad 2:


kwadrat = int(input("Podaj ile liczb podnieść do kwadratu: "))
wynik = 0
list=[]

for i in range(1, kwadrat+1):
    wynik = i * i
    list.append(wynik)

if list == []:
    print("Lista jest pusta")
else:
    print(list)




# zad 3:


ilosc = int(input("Podaj zakres liczb: "))
parzyste = []
nieparzyste = []

for i in range(1, ilosc + 1):
    if i % 2 == 0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)



print("Lista parzysta: ", parzyste)
print()
print("lista nieparzyta: ", nieparzyste)