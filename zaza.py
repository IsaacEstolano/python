salario=float(input("digite seu salario:"))
conta=salario
cheq1=float(input("digite quanto deseja emitir da conta:"))
taxa=0.38
retirada1=cheq1*(taxa/100)
retiradatotal=retirada1+cheq1
conta=conta-retiradatotal
print("o seu saldo bancario é de:",conta)