from prometheus_client import Gauge, start_http_server
from swyftx import SwyftxApi
import logging
import argparse
import time

seconds_per_unit = {"m": 60, "h": 3600}
def convert_to_seconds(s):
    return int(s[:-1]) * seconds_per_unit[s[-1]]

swyftx_api = None
metrics = {'swyftx_api_errors': 0}

def populate_metrics():
  def form_name(code, item_type):
    return "swyftx_" + swyftx_api.get_side() + "_" + code + "_" + item_type + "_" + swyftx_api.get_base_asset() + "_" + swyftx_api.get_resolution()

  if swyftx_api is None:
    return

  latest_bars=swyftx_api.get_latest_bars()

  for code, data in latest_bars.items():
    for item_type in ['open','close','low','high','volume']:
      metric_name = form_name(code, item_type)
      if not metric_name in metrics:
        metrics[metric_name] = Gauge(metric_name, "")

      metrics[metric_name].set(data[item_type])

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--rate", help="The api refresh rate time in minutes or hours, eg 10m, 1h", default="1h")
  parser.add_argument("--resolution", help="The resolution for the candlestick data. Value values are 1m,5m,1h,4h,1d", default="1h")
  parser.add_argument("--side", help="Either bid or ask pricing", default="bid")
  parser.add_argument("--base", help="Base currency code, eg AUD, USD, BTC", default="USD")
  parser.add_argument("--port", help="Port to run the server on", default=8080, type=int)
  parser.add_argument("--log-level", help="The log level for python logging", default="info")
  args = parser.parse_args()

  numeric_level = getattr(logging, args.log_level.upper(), None)
  logging.basicConfig(level=numeric_level)
  logging.info("Exporter starting..")

  rate_in_seconds = convert_to_seconds(args.rate)

  swyftx_api = SwyftxApi(base_asset=args.base, resolution=args.resolution, side=args.side)
  # Populate initial metrics
  populate_metrics()

  start_http_server(args.port)

  sleep_time = rate_in_seconds
  while True:
    time.sleep(sleep_time)
    time_before_populate = time.time()
    populate_metrics()
    time_after_populate = time.time()

    # Account for time taken to populate the metrics
    sleep_time = rate_in_seconds - (time_after_populate - time_before_populate)
    # Leave at least a minute between calls to prevent smashing the api
    if sleep_time < 60:
      sleep_time = 60
