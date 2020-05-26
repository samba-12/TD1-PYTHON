a=int(input ("Donnez A : "))
op=str(input("donnez un operateur "))
b=int(input ("Donnez B : "))
if op =="+":
    resultat=a+b
    print("la somme est",resultat)
elif op=="-":
    resultat=a-b
    print("la soustraction est",resultat)
if op=="/":
    resultat=a/b
    print("la division est",resultat)
elif op =="*":
    resultat=a*b
    print("la multiplication est",resultat)
else:
    print("Erreur")