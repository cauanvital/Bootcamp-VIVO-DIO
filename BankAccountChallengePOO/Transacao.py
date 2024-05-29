from abc import ABC, abstractmethod
from Conta import Conta

class Transacao(ABC):
    def registrar(self, conta:Conta):
        return str(self)
    