vetorV=[]

for i in range(0,3):
    num=int(input("Digite um valor:"))
    vetorV.append(num)
    
def NegativoPor0(vetorA):
    for i in range(0,3):
        if vetorA[i]<0:
            vetorA[i]=0
    return vetorA
vet=NegativoPor0(vetorV)
print(vet)
