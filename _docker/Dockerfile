FROM python:3.11

RUN mkdir /app
COPY ./ /app/
WORKDIR /app
RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi  --no-root
COPY poetry.lock pyproject.toml /app/
COPY .env /app/
RUN poetry install
