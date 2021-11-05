personen = 3
aantalVipminuten = 9

toegangsPrijs = 7.45
vipPrijs = 0.37
totaleSpeelhalbedrag = personen*toegangsPrijs + aantalVipminuten*vipPrijs

speelhaldagTekst = ('Het totale speelhaldag bedrag is ' + str(totaleSpeelhalbedrag) + ' euro voor ' + str(personen) + ' personen en de 45 minuten vip tijd')
print(speelhaldagTekst)
