# 1. Nettoyez les données, vous retirez l'item EURO pour le prix de chaque appareil. 
print("------ première correction ------")

phones = [
    { 'name': "iphone XX", 'priceHT': "900EURO" },
    { 'name': "iphone X", 'priceHT': "70EURO" },
    { 'name': "iphone B", 'priceHT': "200EURO" },
]

phones = [{'name': phone['name'], 'priceHT': float( phone['priceHT'].replace('EURO', '') ) } for phone in phones ]

print(phones)

# une liste de tuples
phones = [ (phone['name'], phone['priceHT']) for phone in phones ]

print(phones)

print("------ deuxième correction ------")

# phones = [
#     { 'name': "iphone XX", 'priceHT': "900EURO" },
#     { 'name': "iphone X", 'priceHT': "70EURO" },
#     { 'name': "iphone B", 'priceHT': "200EURO" },
# ]

# def sanitizeEuro(phones):

#     for phone in phones:
#        phone['priceHT'] = float( phone['priceHT'].replace('EURO', '') )


# sanitizeEuro(phones)
# print(phones)

# le map il itére sur chaque valeur de la liste, une logique pour un item de la liste
# def sanitizeEuro(phone):
#     return { 'name' : phone['name'] , 'priceHT' : float( phone['priceHT'].replace('EURO', '') ) }

# print( list(map(sanitizeEuro, phones)) )

# 2. Créez des tuples à partir des dictionnaires (changement de structure de données)
