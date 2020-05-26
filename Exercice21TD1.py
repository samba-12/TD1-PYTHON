nbre=int(input ("Donnez un nombre : "))
ess=int(input ("devinez le nombre caché : "))
tentative=1
while nbre!=ess:
    if nbre>ess:
        print("Le nombre est plus grand")
        ess=int(input ("devinez le nombre caché : "))
        tentative=tentative+1
    elif nbre<ess:
        print("Le nombre est plus petit")
        ess=int(input ("devinez le nombre caché : "))
        tentative=tentative+1
print("vou avez trouvé le nombre caché en",tentative,"tentatives")


        

    
