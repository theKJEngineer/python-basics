
# set - zestaw to nieuporzadkowany zbior unikalnych wartosci
# frozenset - odmiana set, ktory jest niezmienny 
# np:

set = {0, 4, 8, 12, 16}

set.add(20)                 # dodawanie elementu, jesli dany element istnieje - nie zotanie dodany
set.discard(8)              # usuwanie elementu

frozen = frozenset(set)     # tworzenie frozenset'a czyli podstawienie pod zmienna funkcji 'frozenset(set jako argument)'

setData = {2, 3, 1, 4, 5}
setData.add(22)
setData.discard(1)
print(type(setData))
print(setData)

for i in setData:
    print(i)

frozenData = frozenset(setData)
print(type(frozenData))
# frozenData.add(10)                # bład, nie mozna dodac elementu do frozenset

for i in frozenData:
    print(i)