from sqlalchemy import select, delete, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.materials.schemas import UpdateMaterial, CreateMaterial
from core.Models import Material


async def get_materials(session: AsyncSession) -> list[Material]:
    stmt = select(Material).order_by(Material.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    materials = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    return list(materials)


async def get_material(session: AsyncSession, material_id: int) -> Material | None:
    return await session.get(Material, material_id)


async def remove_material(session: AsyncSession, material_id: int) -> str:
    query = delete(Material).where(Material.id == material_id)
    result: Result = await session.execute(query)
    await session.commit()
    return "Successful"


async def update_material(
    session: AsyncSession, material_id: int, data: UpdateMaterial
) -> str:
    query = (
        update(Material)
        .where(Material.id == material_id)
        .values(
            {
                Material.materialTitle: data.materialTitle,
                Material.quantity: data.quantity,
                Material.unit: data.unit,
                Material.status: data.status,
                Material.min_stock_level: data.min_stock_level,
            }
        )
    )
    await session.execute(query)
    await session.commit()
    return "Successful update!"


async def create_material(
    session: AsyncSession, material_in: CreateMaterial
) -> Material:
    material = Material(**material_in.model_dump())
    # print("material", material.materialname)
    session.add(material)
    await session.commit()
    return material


# async def main():
#     async with db_helper.session_factory() as session:
#         await create_material(session=session, materialname="John")
#         await create_material(session=session, materialname="Sam")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
