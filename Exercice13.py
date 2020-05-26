a=int(input ("Donnez un jour : "))
mois=int(input("donnez un mois "))
b=int(input ("Donnez une année : "))
if mois== 1 or 3 or 5 or 7 or 8 or 10 or 12 :
    if a>1 & a<=31:
        print('La date est valide')
else:
        print('Date invalide')
if mois== 4 or 6 or 9 or 11:
        for a in range(1,30):
            print('La date est valide')
else : 
        print('Date invalide')
if mois ==2:
    for a in range(1,29):
        print('La date est valide')
else:
    print('Date invalide')


