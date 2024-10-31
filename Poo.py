class carro:
    marca=None
    cor=None
    modelo=None
    ano=None
    km_rodados=None
    statusMotor=None
    statusMovimentoCarro=None
    def ligarCarro():
        print("Carro ligado")
    def desligarCarro():
        print("Carro desligado")        
    def andar():
        print("Carro andando")
    def parar():
        print("Carro parado")
        
    def mostrarStatus(self):
        print(f"Marca do carro:{self.marca}")
        print(f"Cor do carro:{self.cor}")
        print(f"Modelo do carro:{self.modelo}")
        print(f"Ano:{self.ano}")
        print(f"Km rodados:{self.km_rodados}")
        print(f"Status do motor:{self.statusMotor}")
        print(f"Status movimento do carro:{self.statusMovimentoCarro}")

Carro=carro()
Carro.statusMotor="Ligado"
Carro.statusMovimentoCarro="Parado"
Carro.marca="Honda"
Carro.cor="Prata"
Carro.modelo="City"
Carro.ano=2011
Carro.km_rodados=40000

Carro.mostrarStatus();