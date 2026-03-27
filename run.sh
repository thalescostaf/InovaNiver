#!/usr/bin/env bash
# Inicializa o ambiente virtual com uv e sobe o servidor
set -e

echo "🚀 Iniciando InovaNiver..."

# Cria/atualiza o ambiente virtual
uv sync

# Sobe o servidor FastAPI
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
