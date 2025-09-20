

print(bool())                   # False brak argumentu


# false values - wartosci ktore daja False przy konwersji na boolean

print(bool(False))              #False  False
print(bool(0))                  #False  0
print(bool(0.0))                #False  0.0  
print(bool( () ))               #False  pusty tuple
print(bool( [] ))               #False  pusta lista
print(bool( {} ))               #False  pusty set
print(bool( "" ))               #False  pusty string
print(bool(None))               #False  w danej zmiennej nie ma wartosci


print(bool(True))               #True   True
print(bool(10))                 #True   liczba rzeczywsita
print(bool(10.30))              #True   liczba zmiennoprzecinkowa
print(bool( ("Adam", 343) ))    #True   Tuple z wartoscia w srodku
print(bool( [3,4,5] ))          #True   lista z zawartoscia
print(bool( {3} ))              #True   set z wartoscia
print(bool("Adam"))             #True   string

