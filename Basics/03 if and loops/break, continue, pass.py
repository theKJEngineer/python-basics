

data = [0,1,2,3,4,5]

for i in data:
    if i == 3:
        break
    print(i*2)


print()



for i in data:
    if i == 3 or i == 5:
        continue
    print(i)



print()

# pass - wypełniacz by kod nie generował błedów


if 10 > 2:      # można ucyć gdy nie mamy dokonczonego kodu
    pass
