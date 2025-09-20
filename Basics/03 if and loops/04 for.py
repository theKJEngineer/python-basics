

for i in [1,2,3,4]:                     #lista
    print(i * 2)

for i in ("Ania", "Ola", "Rafał"):      #tuples
    print(i)

for i in {1,4,6,7,"Ola"}:                #set
    print(i)


for i in "Hello":                       #string
    print(i)
else:
    print("Petla zakonoczona")          # możana dodawać else




dictionaryData = { "Ania" : "ania@przyklad.com", "Adam" : "adam@przyklad.com"}      #słownik

for i in dictionaryData:
    print(i)                              # uzyskamy tylko klucze



for i in dictionaryData.keys():           # tylko klucze ale przez metode keys()
    print(i)  


for key in dictionaryData.keys():
    print(dictionaryData[key])              # tylko wartosci


for key, value in dictionaryData.items():   # para: klucz : wartosc
    print(key," : ", value)


for i in dictionaryData.values():
    print(i)