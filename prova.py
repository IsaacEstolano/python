zaza=[]
numero=0

for i in range(25):
    numero=int(input("Digite um valor"))
    zaza.append(numero)
    zaza[i]=-zaza[i]
j=24
zaza_inverso=[]
numInverso=0
for i in range(25):
    zaza_inverso.append(zaza[j])
    j-=1
print(zaza_inverso)    
