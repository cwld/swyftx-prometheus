FROM python:3.9.2-alpine3.13
RUN apk update && apk add git
RUN mkdir -p /app
COPY ./ /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app/src/
ENTRYPOINT ["python3", "exporter.py"]
