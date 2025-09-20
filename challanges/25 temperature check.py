

raining = False
haveUmbrella = False
temperature = 14

if temperature >= 40 or temperature <= 0:
    print("zostań w domu")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("Możesz wyjść z parasolką")
elif temperature >= 10 and not raining:
    print("Możesz isc bez parasolki")
else:
    print("Zostań w domu")


