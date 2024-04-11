sexo = float(input("Digite 1 se seu sexo for feminino e 2 se seu sexo for masculino: "))
idade = float(input("Digite sua idade: "))

if sexo == 1:
    if idade < 12:
        print("Menina")
    elif 12 <= idade < 24:
        print("Moca")
    else:
        print("Mulher")

elif sexo == 2:
    if idade < 12:
        print("Menino")
    elif 12 <= idade < 24:
        print("Rapaz")
    else:
        print("Homem")

else:
    print("Por favor, digite 1 para feminino ou 2 para masculino.")
