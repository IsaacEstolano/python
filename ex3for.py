maior=None
menor=None
for n in range(10):
    numero=int(input("Digite um numero:"))
    if maior is None or numero > maior:
        maior=numero
    if menor is None or numero < menor:
        menor=numero

print(f"O maior numero e {maior} e o menor e {menor}")    