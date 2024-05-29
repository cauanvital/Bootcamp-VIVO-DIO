from Cliente import Cliente
from Historico import Historico

class Conta:
    def __init__(self,*, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico):
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
    
    def nova_conta(self, cliente, numero):
        pass
    
    def sacar(self, valor) -> bool:
        pass
    
    def depositar(self, valor) -> bool:
        pass
    
class ContaCorrente(Conta):
    def __init__(self, limite:float, limite_saques:int, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo=saldo, numero=numero, agencia=agencia, cliente=cliente, historico=historico)
        self._limite = limite
        self._limite_saques = limite_saques
        
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
