from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua Dos Bobos, 0', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='José Luciano', max_length=30)]
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identidicador do Centro de Treinamento')]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]
