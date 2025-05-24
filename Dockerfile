FROM python:3.12-slim

# Desavativa ambientes virtuais do Poetry (instala no sistema)
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTIONS=1

# Instala o poetry via pip (mais simples e confiável)
RUN pip install poetry

# Define o diretório de trabalho
WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config installer.max-workers 10
RUN poetry install --no-ansi --no-root

# Copia o restante dos arquivos do projeto
COPY . .

CMD ["python", "-m", "scripts.gerar_vendas"]