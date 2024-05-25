from abc import ABC, abstractmethod

usuarios = {}
contas = []

AGENCIA = "0001"
MAXIMO_SAQUES = 3
LIMITE_SAQUE = 500


class Historico:
    def __init__(self, historico):
        self.historico = ""
        self.transacaoId = 0

    def adicionar_transacao(self, transacao):
        self.transacaoId += 1
        self.historico += f"#{self.transacaoId}: Realizada transacao de: {transacao}"

class Conta:
    def __init__(self, numero, cliente, saldo=0.0, agencia=AGENCIA,  historico=""):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico(historico)

    def saldo(self):
        return self.saldo
    
    def nova_conta(cliente, numero):
        return Conta(numero, cliente)

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        self.limite = LIMITE_SAQUE
        self.limite_saques = MAXIMO_SAQUES

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"DEPOSITO no valor de: {self.valor} R$"
    
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"SAQUE no valor de: {self.valor} R$"

class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = contas
    
    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
