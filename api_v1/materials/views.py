from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import Material, UpdateMaterial, CreateMaterial

# from .schemas import CreateMaterial, Material, UpdateMaterial, LoginData


router = APIRouter(tags=["Materials"])


@router.get("/", response_model=list[Material])
async def get_materials(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_materials(session=session)


@router.get("/{material_id}", response_model=Material)
async def get_material(
    material_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    material = await crud.get_material(material_id=material_id, session=session)
    if material is not None:
        return material
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Material {material_id} not found!",
    )


@router.delete("/{material_id}")
async def remove_material(
    material_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    material = await crud.remove_material(material_id=material_id, session=session)
    if material is not None:
        return material
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {material_id} not found!",
    )


@router.post("/", response_model=Material)
async def create_material(
    material: CreateMaterial,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_material(session=session, material_in=material)


@router.patch("/{material_id}")
async def update_material(
    data: UpdateMaterial,
    material_id: int,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    material = await crud.get_material(material_id=material_id, session=session)
    if material is not None:
        return await crud.update_material(
            session=session, data=data, material_id=material_id
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {material_id} not found!",
    )
