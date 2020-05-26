import math
r1=int(input ("Donnez r1 : "))
r2=int(input ("Donnez r2 : "))
r3=int(input ("Donnez r3 : "))
rserie =r1 + r2 +r3

rparal= (r1 * r2 * r3) / (r1*r2 + r2*r3 + r1*r3)
print("la resistance en serie est ", rserie," et le resistance en parallele est ",rparal)