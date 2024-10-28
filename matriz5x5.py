matriz = []

for l in range(0,3):
    linha=[]
    for c in range(0,3):
        num=int(input("Digite um valor:"))
        linha.append(num)
    matriz.append(linha)
soma=0
def somaMatriz (matriz,soma):
    for linha in matriz:
        for num in linha:
            soma=soma+num
    return soma

matrizSoma=somaMatriz(matriz,soma)
print(matrizSoma)