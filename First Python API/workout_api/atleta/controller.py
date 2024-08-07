from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Criar um novo atleta', status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)) -> AtletaOut:
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(nome=atleta_in.categoria.nome))
    ).scalars().first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'A categoria {atleta_in.categoria.nome} não foi encontrada'
        )
        
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=atleta_in.centro_treinamento.nome))
    ).scalars().first()
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'O centro de treinamento {atleta_in.centro_treinamento.nome} não foi encontrado.'
        )
    
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.now(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude=['categoria','centro_treinamento']))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception as e:
        str_exception = str(e)
        str_exception = str_exception[str_exception.index('\nDETAIL: ') + 9:]
        exception_detail = str_exception[:str_exception.index('.\n')]
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Ocorreu um erro ao inserir os dados no banco.{exception_detail}.'
        )
    
    return atleta_out


@router.get('/', summary='Consultar todos os Atletas', status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (
        await db_session.execute(select(AtletaModel))
    ).scalars().all()
    
    return atletas


@router.get('/{id}', summary='Consultar um Atleta pelo id', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def query(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado no id {id}'
        )
    
    return atleta


@router.patch('/{id}', summary='Editar um Atleta pelo id', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def query(id: UUID4, db_session: DatabaseDependency, atleta_upt: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado no id {id}'
        )
        
    atleta_update = atleta_upt.model_dump(exclude_unset=True)
    
    for key, value in atleta_update.items():
        setattr(atleta, key, value)
    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta


@router.delete('/{id}', summary='Deletar um Atleta pelo id', status_code=status.HTTP_204_NO_CONTENT)
async def query(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado no id {id}'
        )

    await db_session.delete(atleta)
    await db_session.commit()
