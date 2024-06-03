#1 criar uma classe Restaurante

class Restaurante:
    nome=''
    categoria=''
    ativo=False


# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()

restaurantes=[restaurante_praca, restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))
print('\n')

# Questão 01)
print('Questão 01)')
restaurante_praca.categoria='Italiana'
print(f'Categoria: {restaurante_praca.categoria}\n')

# Questão 02)
print('Questão 02)')
nome_restaurante=restaurante_praca.nome
print(f'Nome: {nome_restaurante}\n')

# Questão 03) 
'''print('Questão 03)')
estado_restaurante1=restaurante_praca.ativo
estado_restaurante1==False
if(estado_restaurante1==True):
    print(f'O restaurante {restaurante_praca.nome} encontra-se ativo\n')
else:
    print(f'O restaurante {restaurante_praca.nome} encontra-se inativo \n')
'''

# Questão 03 | Corrigida
print('Questão 03)')
if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')
print('')

# Questão 04)
print('Questão 04)')
categoria=Restaurante.categoria
print(f'Categoria: {categoria}\n')

# Questão 05)
'''print('Questão 05)')
nome='Bistrô'
print(f'Nome alterado para: {nome}\n')
'''

# Questão 05 | Corrigida
print('Questão 05)')
restaurante_praca.nome='Bistrô'
print(restaurante_praca.nome)
print('')

# Questão 06)
print('Questão 06)')
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
print(f'Nome: {restaurante_pizza.nome}')
print(f'Categoria: {restaurante_pizza.categoria}\n')

# Questão 07)
print('Questão 07)')
if restaurante_pizza.categoria=='Fast Food':
    print(f'Sim, a categoria do restaurante {restaurante_pizza.nome} é: {restaurante_pizza.categoria}\n')
else:
    print(f'Não, a categoria do restaurante {restaurante_pizza.nome} não é: {restaurante_pizza.categoria}\n')

# Questão 08)
'''print('Questão 08)')
estado_restaurante2=restaurante_pizza.ativo
estado_restaurante2==False
if estado_restaurante2==False:
    print(f'O restaurante {restaurante_pizza.nome} encontra-se ativo\n')
else:
    print(f'O restaurante {restaurante_pizza.nome} encontra-se inativo \n')
'''

# Questão 08 | Corrigida
print('Questão 08)')
restaurante_pizza.ativo=True
print(restaurante_pizza.ativo)
print('')

# Questão 09)
print('Questão 09)')
print(f'Nome: {restaurante_praca.nome}')
print(f'Categoria: {restaurante_praca.categoria}\n')
