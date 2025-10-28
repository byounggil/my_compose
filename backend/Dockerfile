

# FROM python:3.11-slim
FROM python:3.11

# COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
# ✅ ps, curl 설치 (필수 패키지 업데이트 포함)
# RUN apt-get update && apt-get install -y \
#     procps \
#     curl \
# && rm -rf /var/lib/apt/lists/*


WORKDIR /app/
RUN pip install uv




COPY ./pyproject.toml ./uv.lock ./main.py /app/
COPY ./uv.lock /app/

ENV PATH="/app/.venv/bin:$PATH"

RUN uv sync

# RUN --mount=type=cache,target=/root/.cache/uv \
#     uv sync --frozen --no-dev


# CMD ["fastapi", "dev", "app/test.py", "--host", "0.0.0.0"]


# CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload", "--reload-exclude" ,"logs/*"]