
FROM python:3.12


COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install --system -e .

COPY ./src /app/src

EXPOSE 80

CMD ["fastapi", "run", "src/main.py", "--port", "80"]