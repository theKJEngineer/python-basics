str = "Hello"
print(str)
print(len(str)) # metoda len() - zwraca ilosc znaków w stringu liczona od 1


print(str[0])   # wybranie pojedynczego znaku H / indeksowane od 0
print(str[1:4]) # pobranie kilku znaków w danym zakresie indeksów
                # uwaga: ostatni znak nie zostanie pobrany w tym, konsola: ell - od indeksu 1 do 3

print(str*3)    # powtorzy string x3
print(str + "bye bye")  # łaczenie łańcuchów dzieki konkatenacji +


str = """aaaaaaaaaaaaaaaaaaaaaaa
sssssssssssssssssssssssssssssssss
dddddddddddddddddddddddddddddddd
ffffffffffffffffffffffffffffffff""" # blok tekstu, wiekszy string w trzech cudzysłowach, nie ogranicza wielkosci. """" lub '''
print(str)


# \n - znak nowej lini
# \t - znak tabulacji

str = "Pierwsza linia \n druga linia \t tabulacja \n trzecia linia"
print(str)


# zwracanie zawsze ostatniego znaku:
string = "AAAABBBBBCCCCCCD"
print(string[len(string)-1])

print(string[::3])  # wyswietlanie pierwszego znaku + co [3] litery z lancucha znaków