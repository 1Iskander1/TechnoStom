from pydantic import BaseModel, ConfigDict


class MaterialBase(BaseModel):
    materialTitle: str
    quantity: int
    unit: str  # единица измерения
    min_stock_level: int  # Минимальный запас, при котором требуется заказ.
    # category: Mapped[int] = mapped_column(ForeignKey("specs.id"))
    status: str
    category: int


class UpdateMaterial(BaseModel):
    materialTitle: str
    quantity: int
    unit: str  # единица измерения
    min_stock_level: int  # Минимальный запас, при котором требуется заказ.
    # category: Mapped[int] = mapped_column(ForeignKey("specs.id"))
    status: str
    category: int


class CreateMaterial(MaterialBase):
    pass


class Material(MaterialBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
