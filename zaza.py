vetorA=[]
vetorB=[]

for i in range(0,10):
    A=int(input("Digite valores para o vetor a:"))
    B=int(input("Digite valores para o vetor b:"))
    vetorA.append(A)
    vetorB.append(B)

for i in range(0,10):
    print(vetorA[i])
    print(vetorB[i])
def interseccao(a,b):
    conjunto_a=set(a)
    conjunto_b=set(b)
    c=conjunto_a - conjunto_b
    return c

resultado=interseccao(vetorA,vetorB)
print(resultado)