from fastapi import APIRouter, Depends, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import date
from typing import Optional
from app.database import get_db
from app import crud
from app.schemas import AniversarioCreate, AniversarioUpdate

router = APIRouter()
templates = Jinja2Templates(directory="templates")

MESES = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
]

VINCULOS = [
    "Cônjuge", "Filho(a)", "Pai", "Mãe", "Irmão/Irmã",
    "Avô/Avó", "Tio(a)", "Primo(a)", "Amigo(a)", "Colega de trabalho",
    "Cliente", "Parceiro(a)", "Outro",
]


def table_response(request: Request, aniversarios: list, mes_atual: int):
    """Retorna o partial da tabela — request é o 1º arg (Starlette 0.40+)."""
    return templates.TemplateResponse(
        request,
        "partials/table.html",
        {
            "aniversarios": aniversarios,
            "mes_atual": mes_atual,
            "meses": MESES,
            "hoje": date.today(),
        },
    )


@router.get("/", response_class=HTMLResponse)
def index(request: Request, mes: Optional[int] = None, db: Session = Depends(get_db)):
    hoje = date.today()
    mes_filtro = mes if mes else hoje.month
    aniversarios = crud.get_by_month(db, mes_filtro)
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "aniversarios": aniversarios,
            "hoje": hoje,
            "mes_atual": mes_filtro,
            "meses": MESES,
            "vinculos": VINCULOS,
        },
    )


@router.get("/table", response_class=HTMLResponse)
def get_table(request: Request, mes: int, db: Session = Depends(get_db)):
    return table_response(request, crud.get_by_month(db, mes), mes)


@router.post("/aniversarios", response_class=HTMLResponse)
def create_aniversario(
    request: Request,
    nome: str = Form(...),
    data_aniversario: date = Form(...),
    vinculo: str = Form(...),
    telefone: Optional[str] = Form(None),
    mes: int = Form(...),
    db: Session = Depends(get_db),
):
    data = AniversarioCreate(
        nome=nome,
        data_aniversario=data_aniversario,
        vinculo=vinculo,
        telefone=telefone or None,
    )
    crud.create(db, data)
    return table_response(request, crud.get_by_month(db, mes), mes)


@router.get("/aniversarios/{aniversario_id}/edit", response_class=HTMLResponse)
def get_edit_form(
    request: Request, aniversario_id: int, mes: int, db: Session = Depends(get_db)
):
    aniversario = crud.get_by_id(db, aniversario_id)
    if not aniversario:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return templates.TemplateResponse(
        request,
        "partials/modal_form.html",
        {
            "aniversario": aniversario,
            "mes_atual": mes,
            "vinculos": VINCULOS,
        },
    )


@router.put("/aniversarios/{aniversario_id}", response_class=HTMLResponse)
def update_aniversario(
    request: Request,
    aniversario_id: int,
    nome: str = Form(...),
    data_aniversario: date = Form(...),
    vinculo: str = Form(...),
    telefone: Optional[str] = Form(None),
    mes: int = Form(...),
    db: Session = Depends(get_db),
):
    data = AniversarioUpdate(
        nome=nome,
        data_aniversario=data_aniversario,
        vinculo=vinculo,
        telefone=telefone or None,
    )
    crud.update(db, aniversario_id, data)
    return table_response(request, crud.get_by_month(db, mes), mes)


@router.delete("/aniversarios/{aniversario_id}", response_class=HTMLResponse)
def delete_aniversario(
    request: Request,
    aniversario_id: int,
    mes: int,
    db: Session = Depends(get_db),
):
    crud.delete(db, aniversario_id)
    return table_response(request, crud.get_by_month(db, mes), mes)


@router.patch("/aniversarios/{aniversario_id}/toggle", response_class=HTMLResponse)
def toggle_enviada(
    request: Request,
    aniversario_id: int,
    mes: int,
    db: Session = Depends(get_db),
):
    crud.toggle_mensagem_enviada(db, aniversario_id)
    return table_response(request, crud.get_by_month(db, mes), mes)
