import math
i=1
puissance=1
x=int(input ("Donnez La base x : "))
n=int(input ("Donnez la puissance n : "))
for i in range(1,n) : 
    puissance =puissance*x
    print(x," a la puissance ", n ," = ", puissance)