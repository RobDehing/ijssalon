mijn_dictonary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "Registratienummer" : "AA18891"
}
mijn_dictonary["Achternaam"] = "de Vries"
print()
for k, v in mijn_dictonary.items():
    print(k, v)
print(len(mijn_dictonary))
