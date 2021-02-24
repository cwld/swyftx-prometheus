FROM python:3.9.2-alpine3.13
RUN apk update && apk add git
RUN pip install prometheus_client version-query
RUN mkdir -p /app
COPY ./ /app/
WORKDIR /app/src/
ENTRYPOINT ["python3", "exporter.py"]
