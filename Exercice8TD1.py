import math
a=int(input ("Donnez A : "))
b=int(input ("Donnez B : "))
c=int(input ("Donnez C : "))
disc= (b*b)-4*a*c
x=-c/b 
if a==0 & b==0 & c==0 :print('Tout reel est solution')
elif a==0 & b==0 :print('equation na pas de solution')
elif a==0 : print("la solution est x = ",x)
elif disc<0 : print('pas de solution')
else: x1=(-b+math.sqrt(disc))/(2*a)
x2=(-b-math.sqrt(disc))/(2*a)
print("les solutions sont x1 = ",x1," et x2 = ",x2)
