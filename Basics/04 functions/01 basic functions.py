

def addNumber(a, b ):               # a, b - lokalne zmienne, argumenty, dostepne tylko w tej funkcji
    return a + b

def subNumber(a, b):
    return a - b

def multiplyNumber(a, b):
    return a * b

def add4Numbers(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

print(addNumber(10, 5))

number = subNumber(100, 56)
print(number)

number = multiplyNumber(33, 4)
print(number)

sum = add4Numbers(2,addNumber(10, 6),34,number)         # użycie innej funkcji jako argumentu
print(sum)