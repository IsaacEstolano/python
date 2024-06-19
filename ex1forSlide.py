numeroTabuada=int(input("Digite o numero a ser visto a tabuada:"))
num=0
for num in range(11):
    resultado=numeroTabuada*num
    print(f"{numeroTabuada} x {num}= {resultado}")
    num+=num