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
usuarios = {}
contas = []
num_contas = 1

extrato = ''
saldo = 0
num_saques = 0

AGENCIA = "0001"
MAXIMO_SAQUES = 3
LIMITE_SAQUE = 500

menu = """======================================================
Sistema bancário

escolha um caractere para a opção escolhida:
    [u] - criar usuário
    [c] - criar conta
    [lc] - listar contas
    [d] - deposito
    [s] - saque
    [e] - extrato
======================================================

"""

def criarUsuario(usuarios):
    print("Opcao escolhida: criar usuário\n")
    cpf = input("Digite o CPF (somente numeros):")
    if cpf in usuarios.keys():
        print("CPF já existe!")
        return usuarios
    nome = input("Digite o nome do usuário:")
    nascimento = input("Digite a data de nascimento:")
    endereco = input("Digite o endereço:")
    usuarios[cpf] = {"nome": nome, "nascimento": nascimento, "endereco": endereco}
    return usuarios
    

def criarConta(contas, num_contas):
    print("Opcao escolhida: criar conta\n")
    cpf = input("Digite o CPF do titular da conta: ")
    contas.append({"cpf": cpf, "agencia": AGENCIA, "numero": num_contas})
    num_contas += 1
    return contas, num_contas


def listarContas(contas):
    print("Opcao escolhida: listar contas\n")
    if contas: # Testa se existe contas para imprimir
        for conta in contas:
            print(f"AGENCIA: {AGENCIA} || NUMERO: {conta["numero"]} || CPF: {conta["cpf"]}")
    else:
        print(f"Não existem contas para agencia: {AGENCIA}")

    
def Depositar(saldo, extrato):
    print("Opcao escolhida: deposito\n")
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    saldo += valor_deposito
    extrato += f"DEPOSITO: R$ {valor_deposito:.2f}\n"
    return saldo, extrato


def Sacar(**kargs):
    print("Opcao escolhida: saque\n")
    valor_saque = float(input("Digite o valor a ser sacado: "))

    if valor_saque > kargs["saldo"]:
        print("Saldo insuficiente!\n")
    elif valor_saque > LIMITE_SAQUE:
        print("Saque maior que valor permitido por saque (R$ 500.00)!\n")
    elif num_saques >= MAXIMO_SAQUES:
        print("Quantidade diária de saques excedida (3 saques diários)!\n")
    else:
        kargs["num_saques"] += 1
        kargs["saldo"] -= valor_saque
        kargs["extrato"] += f"SAQUE: R$ {valor_saque:.2f}\n"
    return kargs["num_saques"], kargs["saldo"], kargs["extrato"]


def ImprimirExtrato(saldo, extrato):
    # extrato
        print("Opcao escolhida: extrato\n")
        print("============================")
        print(extrato)
        print(f"SALDO: R$ {saldo:.2f}")
        print("============================\n")

print(menu)

while(True):

    operacao = str(input("Digite uma opção: ")).lower()
    if operacao == 'u':
        usuarios = criarUsuario(usuarios)

    elif operacao == 'c':
        contas, num_contas = criarConta(contas, num_contas)

    elif operacao == 'lc':
        listarContas(contas)

    elif operacao == 'd':
        # código para deposito
        saldo, extrato = Depositar(saldo, extrato)

    elif operacao == 's':
        # código saque
        num_saques, saldo, extrato = Sacar(num_saques=num_saques, saldo=saldo, extrato=extrato)

    elif operacao == 'e':
        ImprimirExtrato(saldo, extrato=extrato)
    else:
        #operação inválida
        print("Opcao inválida!")