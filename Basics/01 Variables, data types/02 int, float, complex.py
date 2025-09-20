info = 10
print(type(info))   # funkcja type() zwróci tekst opisujacy typ ktory przechowywany jest wewnatrz zmiennej
                    # typ wynika z wartosci jaka jest przechowywana w zmiennej
                    # w tym przypadku: <class 'int'> - integer - liczba całkowita dodatnia lub ujemna

info = "hello"
print(type(info))   # <class 'str'> - string

x = 3.14
print(type(x))      # <class 'float'> - liczba rzeczywista - zmiennoprzecinkowa

complexNun = 10 + 3j
print(type(complexNun))     # <class 'complex'> - liczba zespolona: część rzeczywista i urojona(oznaczona dodaną litera j)