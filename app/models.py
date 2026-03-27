from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Aniversario(Base):
    __tablename__ = "aniversarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    data_aniversario = Column(Date, nullable=False)
    vinculo = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=True)
    mensagem_enviada = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
