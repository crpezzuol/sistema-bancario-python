# Autor: Carlos Pezzuol
# Data: 2025-04-21
# Versão: 1.0
# Descrição: Sistema bancário simples em Python, com funcionalidades de depósito, saque e extrato.
# O código utiliza funções para organizar as operações e melhorar a legibilidade.
# O código foi escrito para ser executado em um terminal, e não possui interface gráfica.
# Este código é um exemplo de um sistema bancário simples em Python. Ele permite que o usuário faça depósitos, saques e visualize o 
# extrato da conta. O código utiliza funções para organizar as operações e melhorar a legibilidade. O código foi escrito para ser 
# executado em um terminal, e não possui interface gráfica. 
# O código é um exemplo de como utilizar funções, variáveis globais e condicionais em Python. Ele também utiliza a biblioteca os para
# limpar a tela do terminal, dependendo do sistema operacional. O código é um bom exemplo de como criar um sistema simples em Python,
# e pode ser expandido para incluir mais funcionalidades, como transferências entre contas, consulta de saldo, etc.
#
# importando a biblioteca os para limpar a tela do terminal
# e para verificar o sistema operacional
import os

# Definindo as variáveis globais
opcao = ''
saldo = 0
limite_diario = 500
limite_inicial = 500
limite = limite_inicial
extrato = ''
numero_de_saques = 0
limite_de_saques = 3

# Definindo a função limpar_tela para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definindo a função exibir_menu para exibir o menu principal do sistema bancário
# e as informações da conta do usuário
def exibir_menu():
    limpar_tela()
    print(30*'=','Bem vindo ao  Banco Python', 30*'=','\n')
    print(f'Limite da Conta:         R$ {limite_inicial:.2f}')
    print(f'Limite diário de saque:  R$ {limite_diario:.2f}')
    print(f'Saldo atual:             R$ {saldo:.2f}')
    print(f'Saldo + Limite:          R$ {saldo + limite_inicial:.2f}')
    print(f'Número de saques:           {numero_de_saques}\n')
  
# Definindo a função exibir_opcoes para exibir as opções do menu
# e solicitar que o usuário selecione uma opção
def exibir_opcoes():
    print(41*'=','Menu',41*'=','\n')
    print('Selecione uma opção:\n')
    print('[D] Depositar')
    print('[S] Sacar')
    print('[E] Extrato')
    print('[Q] Sair\n')
    print('Selecione uma opção => ', end='')

# Definindo a função depositar para realizar depósitos na conta do usuário
# e atualizar o saldo e o extrato
def depositar(deposito): 
    global saldo, extrato, limite,limite_inicial
    limpar_tela()
    exibir_menu()
    print(39*'=','Deposito',39*'=','\n')
    deposito = float(input('Digite o valor do deposito: R$ '))
    if deposito > 0:
        saldo += deposito
        if limite < limite_inicial:
            limite += deposito
        extrato += f'Deposito: R$ {deposito:.2f}\n'
        print(f'Valor depositado:           R$ {deposito:.2f}')
        print('Deposito realizado com sucesso!', '\n')
        sair = input('Pressione qualquer tecla para continuar...')
        return saldo, extrato, limite
    else:
        deposito <= 0
        print('Valor inválido!')
        print('Valor menor ou igual a zero!')
        sair = input('Pressione qualquer tecla para continuar...')

# Definindo a função sacar para realizar saques na conta do usuário
# e atualizar o saldo, o extrato e o número de saques
def sacar(saque):
    global saldo, extrato, numero_de_saques,limite_diario
    limpar_tela()
    exibir_menu()
    print(40*'=',' Saque',40*'=','\n')
    saque = float(input('Digite o valor do saque: R$ ',))
    if numero_de_saques >= limite_de_saques:
        print('Operação Falhou! Número de saques excedido!\n')
        sair = input('Pressione qualquer tecla para continuar...')
    elif saque > limite_diario:
        print('Operação Falhou! Valor limite diário de saque excedido!\n')
        sair = input('Pressione qualquer tecla para continuar...')
    elif saque <= 0:
        print('Valor inválido!')
        print('Valor menor ou igual a zero!')
        sair = input('Pressione qualquer tecla para continuar...')
    elif saque > limite:
        print('Valor inválido!\n')
        print('Valor maior que o saldo + limite!\n')
        sair = input('Pressione qualquer tecla para continuar...')
    elif saque > saldo:
        sacar_limite(saque)
    elif saque <= saldo and saque <= limite and numero_de_saques < limite_de_saques:
        saldo -= saque
        extrato += f'Saque:    R$ {(saque*(-1)):.2f}\n'
        numero_de_saques += 1
        print(f'Valor sacado: R$ {(saque*(-1)):.2f}')
        print('Saque realizado com sucesso!\n')
        sair = input('Pressione qualquer tecla para continuar...')
    else:
        print('Valor inválido!')

# Definindo a função sacar_limite para realizar saques do limite da conta do usuário
# e atualizar o saldo e o extrato
def sacar_limite(saque):
    global saldo, extrato, numero_de_saques, limite
    if saque > saldo:
        sacar_limite = (input('Valor maior que o saldo! Você vai sacar do limite! (S/N) ').upper())
        if sacar_limite == 'S':
            extrato += f'Saque:    R$ {(saque*(-1)):.2f}\n'
            numero_de_saques += 1
            print(f'Valor sacado: R$ {(saque*(-1)):.2f}')
            print(f'Valor utilizado do limite: R$ {saque - saldo:.2f}')
            limite -= (saque - saldo)
            saldo -= saque
            print('Saque realizado com sucesso!\n')
            sair = input('Pressione qualquer tecla para continuar...')

# Definindo a função exibir_extrato para exibir o extrato da conta do usuário
# e as movimentações realizadas
def exibir_extrato():
    global extrato, saldo
    print(39*'=',' Extrato', 39*'=','\n')    
    print('Não foram realizadas movimentações.\n' if not extrato else extrato)
    print(88*'=','\n')
    sair = input('Pressione qualquer tecla para continuar...')
 
# Início do programa
# Exibindo o menu e as opções para o usuário
while True:

    exibir_menu()
    exibir_opcoes()
    opcao = input().strip().upper() 


    if opcao == 'D':
        depositar(saldo)
                
    elif opcao == 'S':
        sacar(saldo)

    elif opcao == 'E':
        limpar_tela()
        exibir_menu()
        exibir_extrato()


    elif opcao == 'Q' or opcao == 'q':
        limpar_tela()
        print('Saindo...\n')
        break

else:

    print('Operação inválida!, por favor selecione novamente a opção desejada: ')
        