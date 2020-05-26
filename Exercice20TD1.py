a=int(input ("Donnez A : "))
sup=a
i=1
for rang in range(1,10):
    a=int(input ("Donnez A : "))
    if a>sup:
        sup=a
        i=rang
print("le plus grand nombre est ",sup," son rang est ",i)
