
# zad 1

i = 0 
sum = 0

while i <= 100:
    print(i)
    sum = sum + i
    i = i + 1
else:
    print("Koniec petli")


print("Suma wartosci " + str(sum))

print()


# zad 2

list = ["Ania", "Ola", "Kasia", "Daniel"]\

i = len(list)

while i >= 0:
    i = i -1
    print(list[i])
 



# zad 3 


number_of_elements = int(input("Podaj liczbe elementów: "))


sum = 0

if number_of_elements > 0:
    i = number_of_elements

    while i > 0:
        num = float(input("Podaj liczbe: "))
        sum += num
        i -= 1
    average = sum / number_of_elements
else:
    print("Nie mozna obliczyc sredniej")

print("Srednia", average)