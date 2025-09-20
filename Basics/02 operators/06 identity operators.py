
# operatory tożsamosci:

strData = "test"

print(dir(strData))         # pokazuje funkcje jakie mozemy uzyc na tym obiekcie

print(strData.upper())      # tekst duzymi litarami

intData = 10
print(dir(intData))


a = [1, 2, 3, 4, 5]
b = a

print(a is b)               # dwie rozne nazwy ale zmienne wskazuja na to samo miesjce w pamieci czyli REFERENCJA
                            # a is b - czy zmienna a wskazuje na to samo miejsce w pamieci co zmienna b? true
print(b)

a.append(10)                # dodaje 10 do listy a
print(a)                    # 10 dodane do listy
print(b)                    # lista b tez zmieniona

# czyli obie zmienne sa REFERENCJĄ do tego samego miejsca w pamieci gdzie znajduje sie lista
# za pomoca a is b sprawdzamy czy odwolujemy sie do tego samego miejsca w pamieci


print(a is not b)           # false bo wskazuja to samo


