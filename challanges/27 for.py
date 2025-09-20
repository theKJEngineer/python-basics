
# zad 1

list = [-3, -2, -1, 0, 1, 2, 3]
set = {-1}


for i in list:
    if i % 2 != 0:
        set.add(i)


for i in set:
    print(i)



# zad 2

list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]



for i in list:
    if i == 0:
        print("zaro jest pazyste")
    elif i % 2 !=0:
        print(i, "Nieparzyste: ")
        
    else:
        print(i, "Parzyste: ")
       

# zad 3

tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


for i in tuples:
    if i % 2 == 0:
        print(i)