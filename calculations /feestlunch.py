croissantjes = 17
stokbroden = 2
kortingsbonnen = 3

prijsCroissant = 0.39
prijsStokbrood = 2.78
kortingsbonWaarde = 0.50

Croissantbedrag = croissantjes*prijsCroissant
Stokbroodbedrag = stokbroden*prijsStokbrood

Totalebedrag = croissantjes*prijsCroissant + stokbroden*prijsStokbrood - (kortingsbonnen*kortingsbonWaarde)

feestlunchTekst = ('De feestlunch kost bij elkaar ' + str(Totalebedrag) + ' euro voor de ' + str(croissantjes) + ' croissantjes en de ' + str(stokbroden)
    + ' stokbroden en de ' + str(kortingsbonnen) + ' kortingsbonnen als ze nog geldig zijn.')
print(feestlunchTekst)





