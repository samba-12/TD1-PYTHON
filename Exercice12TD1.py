n=int(input ("Donnez A : "))
p=0
i=1
for i in range(1,int(n/2)) : 
        if n%i==0:
            p=p+i
if n==p :
    print('le nombre est parfait')
else :
    print('le nombre nest pas parfait')