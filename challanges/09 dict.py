
config = {
    "website": "example.com",
    "dbType": "mysql",
    "dbUser": "Admin",
    "dbPassword": "12345"
}

print(len(config))

print(config["dbType"])

for i, j in config.items():
    print("Klucz w config: " + i + " z wartoscia: " + j)        # wyswietlanie pary klucz: wartosc za pomoca petli for
