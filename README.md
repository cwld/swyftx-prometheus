# swyftx-prometheus
Prometheus exporter for swyftx candlesticks.
Exports latest candlestick data for all cryptocurrencies, and does not require an API key.

See https://docs.swyftx.com.au/#/reference/charts/latest-bars/get-latest-bars for more info on the api.

## Metric format

Metrics are guages and are named as follows:
```"swyftx_" + <side> + "_" + <coin code> + "_" + <metric type> + "_" + <base asset> + "_" + <resolution>```
eg, *swyftx_ask_BTC_open_AUD_1m*

Additionally there is a *swyftx_api_errors* metric for reporting errors for calls to the api.

## Usage

```
usage: exporter.py [-h] [--rate RATE] [--resolution RESOLUTION] [--side SIDE] [--base BASE] [--port PORT] [--log-level LOG_LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --rate RATE           The api refresh rate time in minutes or hours, eg 10m, 1h
  --resolution RESOLUTION
                        The resolution for the candlestick data. Value values are 1m,5m,1h,4h,1d
  --side SIDE           Either bid or ask pricing
  --base BASE           Base currency code, eg AUD, USD, BTC
  --port PORT           Port to run the server on
  --log-level LOG_LEVEL
                        The log level for python logging
```

## Known issues

At the time of writing, the api was returning invalid data for volume.
