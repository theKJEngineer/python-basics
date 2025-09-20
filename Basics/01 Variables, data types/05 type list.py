

# Lista - uporzadkowana kolekcja wielu elementów odzielonych przecinkiem,
#         zamis w [ ], moze posiadac rozne typy wartosci, przypomina tablice (np z javascript)


list = ['text', 12, "Ania", 99.7]
print(len(list))                       # długosc listy



list = ["Ola", "Ania", 23, 99, "Rafal"]

print(type(list))
print(list)

print(list[0])
print(list[1])
print(list[2])              # elementy listy po indeksach
print(list[3])
print(list[4])

print(list[len(list)-1])    # ostatni element niezaleznie od dlugosci listy

#    print(list[5])         # BŁĄD - elementu o tym indeksie nie ma na liscie


print(list[-1])             # ujemne indexy - liczone od konca  = Rafał
print(list[-2])             # = 99

#    print(list[-6])        # BŁAD - poza zakresem


print(list[1:4])            # pobranie kilku elementów od - do.     print(nazwa[od:do]) - element 'do' nie zostanie pobrany

print(list[2:])             # od indexu 2 do konca listy.           print(nazwa[od:]) 


list[0] = "Kasia"           # zmiana wartosci 
print(list)                 # nowa lista


del list[2]                 # usuwanie lementów z danym indexem
print(list)



print(99 in list)           # sprawdzenie czy dana wartosc znajduje sie na liscie - zwraca True/False
print("Rafal" in list)           
print("Ola" in list)    



if "Ania" in list:          
    print("Ania jest w liscie list")
    print("Kolejny kod")



print("Dalszy kod")         # po 'wyjsciu' ze wciecia w kodzie kod nie podlega pod 'if'



for i in list:              # petla 'for', element listy jeest podstawiany pod 'i' i w bolku kodu można operować na tym elemencie
    print(i)


#                               indexy:
#1     [         0                    1                 2        ]                             
data = [ ["Daniel", "Rafal"], ["Kasia", "Ania"], ["Ola", "Adam"] ]      # lista wielopoziomowa
#2       [   0         1   ]  [   0        1  ]  [  0       1    ]



print(len(data))            # długosc listy 'data' = 3 ponieważ zawiera w sobie trzy inne listy
# index    1  2
print(data[1][0])           # print( nazwaListy [index_1] [index_2] )   = "Kasia"
print(data[2][1])           # = "Adam"


#====================================================================================================



data1 = [1, 2, 3]
data2 = [4, 5, 6]

numbers = data1 + data2         # łaczenie list
print(numbers)



numbersX2 = numbers * 2         # lista x2
print(numbersX2)