limiteinf=int(input("Digite o limite inferior:"))
limitesup=int(input("Digite o limite superior:"))
n=0
soma=0
for n in range(limiteinf,limitesup):
    if n%2 ==0:
        soma+=n
        print(n)
print(f"A somatoria dos numeros pares desse intervalo e:{soma}")