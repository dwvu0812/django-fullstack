FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .

# Make the startup script executable
RUN chmod +x start.sh

EXPOSE 8000

ENTRYPOINT ["./start.sh"]