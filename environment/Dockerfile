FROM python:3.11.9-slim-bookworm

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
COPY solution/ /app/
COPY tests/ /tests/

RUN chmod +x /app/solve.sh
