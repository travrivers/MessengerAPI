FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV MODULE_NAME="app.main"

COPY ./ /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
