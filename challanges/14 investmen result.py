
capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

income = capital * rateOfInterest
incomeResult = income + capital
print("Zwrot wynosi: ", incomeResult)

inflaction = capital * inflationRate
inflationResult = capital - inflaction
print("Wartosc po spadku to ", inflationResult)

total = incomeResult - inflaction
print("Rozliczenie: ", total)