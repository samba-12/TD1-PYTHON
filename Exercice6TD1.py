import math
x1=int(input ("Donnez  x1 : "))
y1=int(input ("Donnez y1 : "))
x2=int(input ("Donnez  x2 : "))
y2=int(input ("Donnez y2 : "))
dist=0
dist= math.sqrt(pow((x1-x2),2) + pow((y1 - y2),2))
print("la distance est ", dist)