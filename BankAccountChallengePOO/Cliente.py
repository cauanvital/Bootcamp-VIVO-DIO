from Conta import Conta
from Transacao import Transacao
from datetime import date

class Cliente:
    def __init__(self,*, endereco:str):
        self._endereco = endereco
        self._contas = []
        
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas
        
    def realizar_transacao(conta:Conta, transacao:Transacao):
        pass
    
    def adicionar_conta(conta:Conta):
        pass
    
class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:date, endereco):
        super().__init__(endereco=endereco)
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
