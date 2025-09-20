

# Tuples - uporzadkowana sekwencja danych, niezmienna kolekcja tworzona za pomoca nawiasów okrągłych 
#          oraz elementów oddzielonych przecinkiem, po utworzeniu nie mozna zmieniać jej elementów np:

data = ("one", "two", "three")
print(type(data))               # <class 'tuple'>
print(data)                     # ("one", "two", "three")


# można zapisać bez ()
data = "one", "two", "three"


# jeśli zawiera jeden element musi miec po nim ',' zeby było wiadomo ze tworzymy tuples a nie ciag znaków
fighters = ("F16",)


# jeśli chce utworzyc pusty tuple to musza być ()
names = ()
print(type(names)) 


# można sobie wyobrazić jako rekord z bazy danych np odnoscie uzytkownika: imie, nazwisko, email itd

# WAZNE: pobieranie elementów działa tak jak w listach
# WAZNE: można tworzyc tuples wielowymiarowy
# WAZNE: wartosc tuple można wielokrotnie powtarzać:
nums = (1,2,3)
print(nums*4)
# WAZNE: łaczenie tuples i sprawdzanie czy element sie w niej znajduje wyglada tak jak w listach
# WAZNE: można uzunać cały tuples ale nie mozna usunac jednego elementu:
del data

# =========================================================================================================

# Do utworzenia tuple mozna uzyć konstruktora 'tuple' :
name = tuple(("Ania", "Asia", "Amelia"))

# =========================================================================================================


data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafal"               # BŁĄD - nie wolno zmianiac elementów

namesss = data + ("Rafał",)
print(len(data))
print(type(namesss))

