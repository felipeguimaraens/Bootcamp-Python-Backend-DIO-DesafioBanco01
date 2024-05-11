"""
Desafio de conta bancária

Operações suportadas: depósito, saque e extrato

DEPOSITO:
    suporta apenas um usuário
    salvar operações em uma variável (para fins de extrato)

SAQUE: 
    máximo de saques diários = 3
    limite por saque = 500 R$
    salvar operações em uma variável (para fins de extrato)

EXTRATO:
    Formato: R$ xxxx.xx 
     
"""

extrato = ''
saldo = 0
num_saques = 0

MAXIMO_SAQUES = 3
LIMITE_SAQUE = 500

menu = """======================================================
Sistema bancário

escolha um caractere para a opção escolhida:
    [d] - deposito
    [s] - saque
    [e] - extrato
======================================================

"""

print(menu)

while(True):

    operacao = str(input("Digite uma opção: ")).lower()
    if operacao == 'd':
        # código para deposito
        print("Opcao escolhida: deposito\n")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo += valor_deposito
        extrato += f"DEPOSITO: R$ {valor_deposito:.2f}\n"

    elif operacao == 's':
        # código saque
        print("Opcao escolhida: saque\n")
        valor_saque = float(input("Digite o valor a ser sacado: "))

        if valor_saque > saldo:
            print("Saldo insuficiente!\n")
        elif valor_saque > LIMITE_SAQUE:
            print("Saque maior que valor permitido por saque (R$ 500.00)!\n")
        elif num_saques >= MAXIMO_SAQUES:
            print("Quantidade diária de saques excedida (3 saques diários)!\n")
        else:
            num_saques += 1
            saldo -= valor_saque
            extrato += f"SAQUE: R$ {valor_saque:.2f}\n"

    elif operacao == 'e':
        # extrato
        print("Opcao escolhida: extrato\n")
        print("============================")
        print(extrato)
        print(f"SALDO: R$ {saldo:.2f}")
        print("============================\n")

    else:
        #operação inválida
        print("Opcao inválida!")



