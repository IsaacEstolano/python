matriz=[]

for l in range(0,3):
    lista=[]
    for c in range(0,3):
        num=int(input("Digite um valor:"))
        lista.append(num)
    matriz.append(lista)

def diagonalPrincipal(matriz):
    soma=0
    for i in range(len(matriz)):
        soma+=matriz[i][i]
    return soma
    
resultado=diagonalPrincipal(matriz)
print(resultado)           


        