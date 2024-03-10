salario=float(input("digite seu salario:"))
conta=salario
cheq1=float(input("digite quanto deseja emitir da conta:"))
taxa=0.38
retirada1=cheq1*(taxa/100)
retiradatotal1=retirada1+cheq1
conta=conta-retiradatotal1
cheq2=float(input("digite o saldo a emitir da conta para o cheque 2:"))
retirada2=cheq2*(taxa/100)
retiradatotal2=retirada2+cheq2
conta=conta-retiradatotal2
print("o seu saldo bancario é de:",conta)