
dogAge = float(input("Podaj wiek psa: "))
humanAge = 0

if dogAge == 1:
    humanAge = 15
    print(humanAge)
elif dogAge == 2:
    humanAge = 15 + 9
    print(humanAge)
elif dogAge >= 3:
    humanAge = 24 + (dogAge - 2) * 5
    print(humanAge)
else:
    print("Podaj prawidlowa wartosci")



