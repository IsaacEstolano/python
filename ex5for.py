n=0
contador=0
for n in range(15):
    n=int(input("Digite um numero:"))
    if n>30:
        contador+=1

print(f"Foram digitados {contador} maiores que 30")        