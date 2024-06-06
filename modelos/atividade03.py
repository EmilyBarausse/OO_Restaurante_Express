# #Exemplo:
# print('Exemplo')
# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo=titulo
#         self.autor=autor
#         self.paginas=paginas
#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def aumentar_paginas(self,quantidade):
#         self.paginas += quantidade

# livro1=Livro('Tanto Faz','Jão',50)
# print(livro1)

# livro1.aumentar_paginas(90)
# print(livro1)
# print('')



# # Questão 01
# print('Questão 01)')
# class Pessoa:

#     def __init__(self,nome,idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao

#     def __str__(self):
#             return f'{self.nome} | {self.idade} anos | {self.profissao}'

#     def aniversario(self):
#         self.idade += 1
    
#     @property
#     def saudacao(self):
#         if self.profissao:
#             print(f'Olá, sou {self.nome}! Trabalho como {self.profissao}.') 
#         else:
#             print(f'Olá, sou {self.nome}!') 

# pessoa_1=Pessoa('Ronaldo',40,'Operador de máquina') 
# print(pessoa_1)
# pessoa_1.aniversario()
# print(pessoa_1)
# print('')
# pessoa_1.saudacao
# print('')


# # Questão 02, 03 e 04
# print('Questão 02 | 03 | 04)')
# class ContaBancaria:
    
#     #Q02
#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#         self._ativo=False #atributo protegido
        
#     #Q03
#     def __str__(self):
#         return f'Titular da conta bancária: {self.titular} | Saldo disponível: R$ {self.saldo}'

# # conta1=ContaBancaria('Arina da Piedade', 3,58)

# # conta2=ContaBancaria('Rosicléa da Aparecida', 1256,27)
    
# # print(conta1)
# # print('')
# # print(conta2)
# # print('')

#     #Q04     
#     @classmethod   
#     def ativar_conta(cls,conta):
#         conta._ativo= True
        
# conta3=ContaBancaria('José', 10,00)
# print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativar: Conta ativa? {conta3._ativo}')
            

# # Questão 05 
# class ContaBancariaPythonica:
#     def __init__(self,titular,saldo):
#         self._titular=titular
#         self._saldo=saldo
#         self._ativo=False
        
#     @property
#     def titular(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo

# # Questão 06 
# conta4=ContaBancariaPythonica('Josefino',1500,2)
# print(f'Titular da conta 4 é: {conta4.titular}')

# Questão 07
# print('Questão 07')
class ClienteBanco:
    
    def __init__(self,nome,idade,cpf,telefone,cidade):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        self.telefone=telefone
        self.cidade=cidade
        
# cliente1=ClienteBanco('João Moreira', '55 anos', '089.487.264-14', '(41) 99487-6538', 'Campo Largo')
# cliente2=ClienteBanco('Eliane Quirino', '47 anos', '099.325.584-27', '(41) 99981-0568', 'Balsa Nova')
# cliente3=ClienteBanco('Maria Silva', '32 anos', '095.789.123-45', '(41) 98826-1414', 'Curitiba')

# Questão 08
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta
    
conta_cliente1=ClienteBanco.criar_conta('Tertulia',9999.99)
print(f'Conta de {conta_cliente1.titular} com saldo de R$ {conta_cliente1.saldo_inicial}')