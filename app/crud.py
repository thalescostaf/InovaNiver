from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models import Aniversario
from app.schemas import AniversarioCreate, AniversarioUpdate
from datetime import date
from typing import Optional


def get_all(db: Session) -> list[Aniversario]:
    return db.query(Aniversario).order_by(
        extract("month", Aniversario.data_aniversario),
        extract("day", Aniversario.data_aniversario),
    ).all()


def get_by_month(db: Session, month: int) -> list[Aniversario]:
    return (
        db.query(Aniversario)
        .filter(extract("month", Aniversario.data_aniversario) == month)
        .order_by(extract("day", Aniversario.data_aniversario))
        .all()
    )


def get_by_id(db: Session, aniversario_id: int) -> Optional[Aniversario]:
    return db.query(Aniversario).filter(Aniversario.id == aniversario_id).first()


def create(db: Session, data: AniversarioCreate) -> Aniversario:
    aniversario = Aniversario(**data.model_dump())
    db.add(aniversario)
    db.commit()
    db.refresh(aniversario)
    return aniversario


def update(db: Session, aniversario_id: int, data: AniversarioUpdate) -> Optional[Aniversario]:
    aniversario = get_by_id(db, aniversario_id)
    if not aniversario:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(aniversario, field, value)
    db.commit()
    db.refresh(aniversario)
    return aniversario


def delete(db: Session, aniversario_id: int) -> bool:
    aniversario = get_by_id(db, aniversario_id)
    if not aniversario:
        return False
    db.delete(aniversario)
    db.commit()
    return True


def toggle_mensagem_enviada(db: Session, aniversario_id: int) -> Optional[Aniversario]:
    aniversario = get_by_id(db, aniversario_id)
    if not aniversario:
        return None
    aniversario.mensagem_enviada = not aniversario.mensagem_enviada
    db.commit()
    db.refresh(aniversario)
    return aniversario
