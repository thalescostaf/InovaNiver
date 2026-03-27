from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routers.birthdays import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="InovaNiver - Sistema de Aniversários")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
