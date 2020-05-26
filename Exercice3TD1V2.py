import math
r1=int(input ("Donnez r1 : "))
r2=int(input ("Donnez r2 : "))
r3=int(input ("Donnez r3 : "))
c=int(input ("faites un choix 1 pour la resistance serie et 2 pour la resistance en parallele "))
if c ==1 : rserie =int(r1 + r2 +r3)
print("la resistance en serie est ", rserie)

if c ==2 : rparal= int((r1 * r2 * r3) / (r1*r2 + r2*r3 + r1*r3))
print("la resistance en parallele est ",rparal)