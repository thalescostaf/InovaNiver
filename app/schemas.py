from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional


class AniversarioBase(BaseModel):
    nome: str
    data_aniversario: date
    vinculo: str
    telefone: Optional[str] = None
    mensagem_enviada: bool = False


class AniversarioCreate(AniversarioBase):
    pass


class AniversarioUpdate(BaseModel):
    nome: Optional[str] = None
    data_aniversario: Optional[date] = None
    vinculo: Optional[str] = None
    telefone: Optional[str] = None
    mensagem_enviada: Optional[bool] = None


class AniversarioOut(AniversarioBase):
    id: int

    class Config:
        from_attributes = True
