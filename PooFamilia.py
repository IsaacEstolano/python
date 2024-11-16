class pessoa:
    def _init(self,nome,idade,endereco,cpf):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cpf=cpf
    nome=None
    idade=None
    endereco=None
    cpf=None
    sexo=None
    def resumo(self,_nome,_idade,_endereco,_cpf,):
        print(f"Nome:{_nome}/n Idade={_idade}/n Endereco:{_endereco}/n Cpf:{_cpf}/n ")
class pai(pessoa):
    def _init(self, nome, idade, endereco, cpf):
        super()._init(nome, idade, endereco, cpf)
    
    filho=None
    esposo=None
    
    def resumoPai(self,_filho,_esposa):
        print(f"Esposo de {_esposa} e pai de {_filho}")
class mae(pessoa):
    def _init(self, nome, idade, endereco, cpf):
        super()._init(nome, idade, endereco, cpf)
    filho=None
    esposa=None
    
    def resumoMae(self,_esposo,_filho):
        print(f"Esposa de {_esposo} /n Mae de {_filho}")
    
class filho(pessoa):
    pai=None
    mae=None
    
    def resumofilho(self,_mae,_pai):
        print(f"Filho de {_pai} e {_mae}")
        

Pai=pai()
pai.nome="Gustavo"
pai.cpf=1234567
pai.endereco="Camboriu"
pai.esposo=True    
pai.filho=True
pai.idade=53

Mae=mae()
mae.nome="Franqueline"
mae.cpf=7654321
mae.endereco="Camboriu"
mae.esposa=True
mae.filho=True
mae.idade=50

Filho=filho()
filho.nome="Isaac"
filho.cpf=5816641
filho.endereco="Camboriu"
filho.pai=True
filho.mae=True
filho.idade=17

pai.resumo(pai.nome,pai.idade,pai.endereco,pai.cpf)
pai.resumoPai(pai.nome,filho.nome,mae.nome)
    

    