a=int(input ("Donnez un jour : "))
mois=int(input("donnez un mois "))
b=int(input ("Donnez une année : "))
if b%4==0 & b%100==0 & b%400==0:
    print("L'annee est bisextile")
else:
    print("L'annee n'est pas bisextile")




