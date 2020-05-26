a=int(input ("Donnez A : "))
b=int(input ("Donnez B : "))
c=a
d=b
while a!=b:
    if a>b :
        b=b+d
    elif a<b:
        a=a+c
print("Le PPCM est ",b)