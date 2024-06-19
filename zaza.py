nome=input("Digite seu nome:")
while len(nome)<=3:
    nome=input("Digite seu nome:(Necessario mais que 3 caracteres)")
idade=int(input("Digite sua idade:"))
while (idade<=0 or idade>150):
    idade=int(input("Digite sua idade:(Necessario ser menor que 150 e maior que 0)"))
salario=float(input("Digite seu salario:"))
while(salario<=0):
    salario=float(input("Digite seu salario:(Necessario ser maior que 0)"))
sexo=input("Digite seu sexo:")
while(sexo!='f' and sexo!="m"):
    sexo=input("Digite seu sexo(Necessario ser f para feminino e m para masculino)")
estadoCivil=input("Digite seu estado civil:")
while(estadoCivil!="s" and estadoCivil!="c" and estadoCivil!="v" and estadoCivil!="d"):
    estadoCivil=input("Digite seu estado civil:(Necessario s para solteiro,c para casado,v para viuvo ou d para divorciado)")