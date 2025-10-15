FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]