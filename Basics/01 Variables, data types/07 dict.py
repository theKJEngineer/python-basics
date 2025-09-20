
# Słownik - sposob na przechowywanie danych za pomoca kluczy oraz wartosci, klucze musza byc unikalne
#           i po : jest wartosc dal danego klucza, elementy w slowniku nie maja kolejnosci ale mozna pobrac ilosc elementow



contacts = {                        # słownik
    "Ola": "ola@example.com",
    "Daniel": 30,                   # pary klucz : wartosc
    "Ania": "ania@example.com"
}

contacts["Rafal"] = "rafal@examplecom"  # dodawanie nowego klucza do slownika

print(contacts["Ola"])                  # terminal: ola@example.com
print(contacts["Daniel"])

print(type(contacts))

print(len(contacts))                    # ilosc elementow w slowniku. 
                                        # UWAGA nie jest to lista, elementy sa umieszczone losowo

print(contacts.keys())                  # wyswietli wszystkie klucze wewnatrz slownika
print(contacts.values())                # wyswietli wszystkie wartoscie ze slownika

for i in contacts:                      # iteracja za pomoca key
    print(i +" "+ str(contacts[i]))     # funkcaj str() konwertuje dowolny typ na lancuch znakow


for i, j in contacts.items():
    print(i, " ", j)                               
