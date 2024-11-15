class pessoa:
    def _init(self,nome,idade,endereco,cpf,sexo):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cpf=cpf
        self.sexo=sexo
    nome=None
    idade=None
    endereco=None
    cpf=None
    sexo=None
    def resumo(self):
        print(f"Nome:{self.nome}/n Idade={self.idade}/n Endereco:{self.endereco}/n Cpf:{self.cpf}/n Sexo:{self.sexo}/n")
class pai(pessoa):
    filhos=None
    esposo=None
    
    def resumoPai(self,_pai):
        print(f"É pai de {_pai}")
class mae(pessoa):
    filhos=None
    esposa=None
    def resumoMae(self)
    
class filho(pessoa):
    pai=None
    mae=None

    

    