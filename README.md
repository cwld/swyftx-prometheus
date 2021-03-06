# swyftx-prometheus
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/clml/swyftx-prometheus-exporter)

Prometheus exporter for swyftx candlesticks.
Exports latest candlestick data for all cryptocurrencies, and does not require an API key.

See https://docs.swyftx.com.au/#/reference/charts/latest-bars/get-latest-bars for more info on the api.

## Metric format

Metrics are guages and are named and have labels as follows:

```swyftx_<metric_type>_<resolution>{base="<base asset>",coin="<coin code>",side="<side>"}```

eg, *swyftx_open_1m{base="AUD",coin="AMB",side="ask"} 0.053803080708461334*

Additionally there is a *swyftx_api_errors* metric for reporting errors for calls to the api.

## Usage

```
usage: exporter.py [-h] [--rate RATE] [--resolution RESOLUTION] [--side SIDE] [--base BASE] [--port PORT] [--log-level LOG_LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --rate RATE           The api refresh rate time in minutes or hours, eg 10m, 1h. Default 1h
  --resolution RESOLUTION
                        The resolution for the candlestick data. Value values are 1m,5m,1h,4h,1d. Default 1h
  --side SIDE           Either bid or ask pricing. Default bid
  --base BASE           Base currency code, eg AUD, USD, BTC. Default USD
  --port PORT           Port to run the server on. Default 8080
  --log-level LOG_LEVEL
                        The log level for python logging. Default info
```

## Dockerhub

https://hub.docker.com/r/clml/swyftx-prometheus-exporter

## Known issues

At the time of writing, the api was returning invalid data for volume.
