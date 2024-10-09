conjunto1={2,4,8,10}
conjunto2={1,3,5,7,9}

print("A uniao dos conjuntos:")
print(conjunto1 | conjunto2)
print("A interseccao dos conjuntos:")
if conjunto1 & conjunto2:
    print(conjunto1 & conjunto2)
else:
    print("Nao ha interseccao entre os conjuntos")
