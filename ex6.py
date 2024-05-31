n=0
positivos=0
negativos=0
somaPositivos=0
contadorNegativos=0
for n in range(20):
    n=int(input("Digite um numero:"))
    if n>0:
        somaPositivos+=n
    elif n<0:
        contadorNegativos+=1
print(f"A somatoria dos numeros positivos e {somaPositivos} e a quantidade de numeros negativos e {contadorNegativos}")