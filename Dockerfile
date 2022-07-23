ARG PYTHON_VERSION=3.10.5
ARG POETRY_VERSION=1.1.14



FROM python:${PYTHON_VERSION}-slim AS build

ENV PYTHONUNBUFFERED=1
WORKDIR /app

ARG POETRY_VERSION
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock /app/
RUN poetry export -o /requirements.txt



FROM python:${PYTHON_VERSION}-slim

ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
VOLUME /www
WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY --from=build /requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && \
    rm -f /requirements.txt && \
    pip install --no-cache-dir gunicorn==20.1.0 && \
    apt-get autoremove -y build-essential && \
    apt-get clean

COPY site /app

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
