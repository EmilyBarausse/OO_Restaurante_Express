# Questão 01
# print('Questão 01)')
# class Pessoa:
#     pessoas=[]

#     def __init__(self,nome,profissao,idade=0):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao

#         Pessoa.pessoas.append(self)

#     def __str__(self):
#             return f'{self.nome} | {self.idade} | {self.profissao}'
    
#     def listar_pessoas():
#         for pessoas in Pessoa.pessoas:
#             print(f'Nome: {pessoas.nome} | Idade: {pessoas.idade} | Profissão: {pessoas.profissao}')
            
#     def aumentar_idade(self, valor):
#         self.idade += valor
        

# pessoa_1=Pessoa('Ronaldo','40','Operador de máquina') 
# pessoa_1.aumentar_idade()

# Pessoa.listar_pessoas()
# print('')




# Questão 02, 03 e 04
print('Questão 02 | 03 | 04)')
class ContaBancaria:
    conta_bancaria=[]
    
    #Q02
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False
        
        ContaBancaria.conta_bancaria.append(self)
        
    #Q03
    def __str__(self):
        return f'{self.titular} | {self.saldo}'
    
    def listar_conta_bancaria():
        for conta_bancaria in ContaBancaria.conta_bancaria:
            print(f'Titular da conta bancária: {conta_bancaria.titular}. Saldo disponível: {conta_bancaria.saldo}. Status ativação: {conta_bancaria.ativo}')
    
    #Q04        
    def ativar_conta(self):
        self.ativo= not self.ativo
            
conta_bancaria_1=ContaBancaria('Arina da Piedade','R$ 3,58')
conta_bancaria_1.ativar_conta()

conta_bancaria_2=ContaBancaria('Rosicléa da Aparecida','R$ 1256,27')
conta_bancaria_2.ativar_conta()

ContaBancaria.listar_conta_bancaria()
print('')


# Questão 05 ???????????????????????????????????????????????????????????


# Questão 06 ???????????????????????????????????????????????????????????


# Questão 07
print('Questão 07')
class ClienteBanco:
    
    def __init__(self,nomeCliente,idadeCliente,cpfCliente,telefoneCliente,cidadeCliente):
        self.nomeCliente=nomeCliente
        self.idadeCliente=idadeCliente
        self.cpfCliente=cpfCliente
        self.telefoneCliente=telefoneCliente
        self.cidadeCliente=cidadeCliente
        
    @classmethod
    def listar_clientes():
        print(f'{'Nome'.ljust(30)} | {'Idade'.ljust(30)} | {'CPF'.ljust(30)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
        
cliente1=ClienteBanco('João Moreira', '55 anos', '089.487.264-14', '(41) 99487-6538', 'Campo Largo')
cliente2=ClienteBanco('Eliane Quirino', '47 anos', '099.325.584-27', '(41) 99981-0568', 'Balsa Nova')
cliente3=ClienteBanco('Maria Silva', '32 anos', '095.789.123-45', '(41) 98826-1414', 'Curitiba')
