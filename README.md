<h1 align="center">InovaNiver</h1>

<p align="center">
  Sistema de registro e notificação de aniversários da <strong>Inovamind</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-012169?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009cde?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-14%2B-012169?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/HTMX-2.0-009cde?style=flat-square" />
</p>

---

## Objetivo

O **InovaNiver** centraliza o registro de aniversários de clientes, parceiros, colaboradores e familiares, garantindo que nenhuma data passe em branco.

A aplicação exibe os aniversariantes do mês corrente, destaca quem faz aniversário **hoje**, permite enviar parabéns diretamente pelo **WhatsApp** e controla quem já recebeu a mensagem — tudo em uma única página, sem recarregamentos.

---

## Funcionalidades

| Funcionalidade | Detalhe |
|---|---|
| Tabela de aniversariantes | Filtrada pelo mês atual por padrão |
| Filtro por mês | Selecione qualquer mês do ano |
| Destaque do dia | Linha em amarelo + badge "Hoje!" para o aniversariante do dia |
| Enviar parabéns | Abre o WhatsApp Web com mensagem pré-preenchida (quando há telefone) ou copia a mensagem |
| Controle de envio | Toggle "Enviado" por aniversariante |
| CRUD completo | Adicionar, editar e excluir sem sair da página (modal + HTMX) |
| Header fixo | Logo Inovamind visível em toda a navegação |

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12 |
| Gerenciador de ambiente | [uv](https://docs.astral.sh/uv/) |
| Framework web | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM | [SQLAlchemy 2](https://www.sqlalchemy.org/) |
| Banco de dados | PostgreSQL 14+ |
| Templates | Jinja2 (server-side rendering) |
| Interatividade | [HTMX 2](https://htmx.org/) |
| Estilo | CSS puro (identidade visual Inovamind) |

---

## Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) instalado (`pip install uv` ou `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- PostgreSQL 14+ rodando localmente ou acessível via rede

---

## Configuração do banco de dados

### 1. Criar o banco

Conecte-se ao PostgreSQL e execute:

```sql
CREATE DATABASE inovaniver;
```

### 2. Criar as tabelas

Execute o script SQL incluído no projeto:

```bash
psql -U seu_usuario -d inovaniver -f sql/create_tables.sql
```

Ou copie e execute o conteúdo de [sql/create_tables.sql](sql/create_tables.sql) diretamente no seu cliente SQL (DBeaver, pgAdmin, etc.).

O script cria:
- A tabela `aniversarios` com todos os campos necessários
- Índices para consultas rápidas por mês
- **Dados de exemplo** no mês atual (remova antes de ir para produção)

---

## Como rodar o projeto

### 1. Clone e entre na pasta

```bash
git clone <url-do-repositorio>
cd InovaNiver
```

### 2. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/inovaniver
```

### 3. Instale as dependências

```bash
uv sync
```

### 4. Adicione a logo

Salve o arquivo da logo Inovamind em:

```
static/images/logo.png
```

### 5. Suba o servidor

```bash
uv run uvicorn main:app --reload
```

Acesse no navegador: **http://localhost:8000**

> Para rodar em modo produção (sem reload):
> ```bash
> uv run uvicorn main:app --host 0.0.0.0 --port 8000
> ```

---

## Estrutura do projeto

```
InovaNiver/
├── pyproject.toml              # Dependências e configuração do projeto
├── .env.example                # Template de variáveis de ambiente
├── main.py                     # Entry point da aplicação
├── sql/
│   └── create_tables.sql       # Script de criação do banco
├── app/
│   ├── config.py               # Leitura de variáveis de ambiente
│   ├── database.py             # Conexão e sessão com o PostgreSQL
│   ├── models.py               # Modelo ORM (tabela aniversarios)
│   ├── schemas.py              # Validação de dados (Pydantic)
│   ├── crud.py                 # Operações de banco de dados
│   └── routers/
│       └── birthdays.py        # Rotas da aplicação
├── templates/
│   ├── base.html               # Layout base com header fixo
│   ├── index.html              # Página principal
│   └── partials/
│       ├── table.html          # Tabela de aniversariantes (HTMX)
│       └── modal_form.html     # Formulário de edição (HTMX)
└── static/
    ├── css/style.css           # Estilos (identidade Inovamind)
    ├── js/app.js               # Modal, toast e clipboard
    └── images/
        └── logo.png            # Logo Inovamind (adicionar manualmente)
```

---

<p align="center">
  Desenvolvido por 
  <strong>
    <a href="https://thalesfernandes.dev" target="_blank">
      Thales Fernandes
    </a>
  </strong>
  com 
  <strong>
    <a href="https://inovamind.dev" target="_blank">
      INOVAMIND
    </a>
  </strong>

</p>
