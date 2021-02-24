FROM python:3.9.2-alpine3.13
RUN pip install prometheus_client
RUN mkdir -p /app
WORKDIR /app
COPY ./src/*.py /app
ENTRYPOINT ["python3", "exporter.py"]
