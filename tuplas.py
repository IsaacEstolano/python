fruta = ("maçã", "banana", "laranja", "abacaxi", "uva")
UserFruta=(input("Digite uma fruta:"))
if UserFruta in fruta:
    print(f"{UserFruta} esta na tupla")
else:
    print(f"{UserFruta} nao esta a tupla")