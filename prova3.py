zaza=[]
numero=0
pares=0
medImpar=0
armaz=0
impares=0
armazenar=0
for i in range(8):
    numero=int(input("Digite um valor"))
    zaza.append(numero)
    if zaza[i]%2==0:
        pares+=1
    if zaza[i]%2!=0:
        armaz=(zaza[i])
        impares+=1
        armazenar+=armaz
        medImpar=armazenar/impares        
print(pares)
print(medImpar)