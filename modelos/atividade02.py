# Questão 01
print('Questão 01)')
class Carro:
    carros=[]

    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano

        Carro.carros.append(self)

    def __str__(self):
            return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carros in Carro.carros:
            print(f'{carros.modelo} | {carros.cor} | {carros.ano}')

carro_1=Carro('Fusca','Azul','1985') 

carro_2=Carro('Brasilia','Amarela','1973')

Carro.listar_carros()
print('')

# Questão 02 e 03
print('Questão 02 e 03)')
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,telefone,cidade):
        self.nome=nome
        self.categoria=categoria
        self.telefone=telefone
        self.cidade=cidade
        self.ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
            return f'{self.nome} | {self.categoria} | {self.telefone} | {self.cidade}'
     
    def listar_restaurantes():
        for restaurantes in Restaurante.restaurantes:
            print(f'{restaurantes.nome} | {restaurantes.categoria} | {restaurantes.telefone} | {restaurantes.cidade} | {restaurantes.ativo}')

restaurante_1=Restaurante('O Trailer','Hamburgueria','(41) 98659-9771', 'Campo Largo') 

restaurante_2=Restaurante('Primos','Pizzaria','(41) 99642-8526', 'Campo Largo')

Restaurante.listar_restaurantes()
print('')


# Questão 04
print('Questão 04)')
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria,telefone,cidade):
        self.nome=nome
        self.categoria=categoria
        self.telefone=telefone
        self.cidade=cidade
        self.ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
            return f'{self.nome} | {self.categoria} | {self.telefone} | {self.cidade}'
     
    def listar_restaurantes():
        for restaurantes in Restaurante.restaurantes:
            print(f'O restaurante {restaurantes.nome} pertence à categoria de {restaurantes.categoria}. Seu telefone para contato é {restaurantes.telefone} e está localizado em {restaurantes.cidade}.')

restaurante_1=Restaurante('O Trailer','Hamburgueria','(41) 98659-9771', 'Campo Largo') 

restaurante_2=Restaurante('Primos','Pizzaria','(41) 99642-8526', 'Campo Largo')

Restaurante.listar_restaurantes()
print('')


# Questão 05
print('Questão 05)')
class Cliente:
    clientes=[]

    def __init__(self,nome,idade,cpf,telefone):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        self.telefone=telefone

        Cliente.clientes.append(self)

    def __str__(self):
            return f'{self.nome} | {self.idade} | {self.cpf} | {self.telefone}'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.cpf} | {cliente.telefone}')

cliente_1=Cliente('Wilson','77','003.659.687-12','(41)3292-0879') 

cliente_2=Cliente('Aniceto','63','008.479.128-23','(41) 99139-1698')

Cliente.listar_clientes()
print('')