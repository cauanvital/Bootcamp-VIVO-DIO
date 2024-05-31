from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta) -> None:
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta) -> None:
        sucesso = conta.depositar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao) -> None:
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data/hora": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor) -> bool:
        try:
            self._saldo = float(self.saldo)
            valor = float(valor)
        except:
            return False
        
        if valor > self.saldo:
            return False
        else:
            self._valor -= valor
            return True
    
    def depositar(self, valor) -> bool:
        try:
            self._saldo = float(self.saldo)
            valor = float(valor)
            self._saldo += valor
        except:
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
        
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
    
    def sacar(self, valor):
        try:
            self._saldo = float(self.saldo)
            valor = float(valor)
        except:
            return False
        
        if self.limite_saques == 0:
            return False
        elif valor > self.limite:
            return False
        elif valor > self.saldo:
            return False
        else:
            self._limite_saques -= 1
            self._valor -= valor
            return True
    
class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas
        
    def realizar_transacao(self, conta, transacao) -> None:
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        
    @property
    def cpf(self):
        return self._cpf
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def data_nascimento(self):
        return self._data_nascimento
