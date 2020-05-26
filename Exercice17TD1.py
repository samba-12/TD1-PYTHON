a=int(input ("Donnez A : "))
b=int(input ("Donnez B : "))
while a>b:
    a=a-b
    if a==b:
        print("le pgcd est",a)
while a<b:
    b=b-a
    if a==b:
        print("le pgcd est",a)


