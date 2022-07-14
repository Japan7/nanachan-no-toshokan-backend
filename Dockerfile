FROM python:3.10.5-slim AS build

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry export -o /requirements.txt



FROM python:3.10.5-slim

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
    pip install --no-cache-dir gunicorn && \
    apt-get autoremove -y build-essential && \
    apt-get clean

COPY . /app

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
