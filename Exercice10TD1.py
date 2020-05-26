a=int(input ("Donnez A : "))
b=int(input ("Donnez B : "))
c=int(input ("Donnez C : "))
if a>b & b>c :
     i=a 
     a=c 
     c=i
     print("lordre est",a,b,c)
elif b>a & a>c :
     i=b 
     b=c 
     c=i
     print('lordre est' ,b,a,c)
elif c>b & b>a :
     i=c 
     c=a 
     a=i
     print('lordre est' ,c,b,a)
elif c>a & a>b :
     i=c 
     c=b 
     b=i
     print('lordre est' ,c,a,b)
elif a>c & c>b :
     i=a 
     a=b 
     b=i
     print('lordre est' ,a,c,b)
elif b>c & c>a :
     i=b 
     b=a 
     a=i
     print('lordre est' ,b,c,a)
else:
    print("erreur")