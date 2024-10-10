zaza=[]
i=0 
positivos=[]
negativos=[]

for i  in range(8):
    numero=int(input("Digite um valor:"))
    zaza.append(numero)
    if zaza[i]>0:
        positivos.append(zaza[i])
    if zaza[i]<0:
        negativos.append(zaza[i])

print(f"Positivos:{positivos}")
print(f"Negativos:{negativos}")        
