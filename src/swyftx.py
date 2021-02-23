import json
import logging
import urllib.request

SWYFTX_API_BASE="https://api.swyftx.com.au/"
SWYFTX_LATEST_BAR="charts/getLatestBar/"
SWYFTX_BASIC_INFO="markets/info/basic/"


def RequestApi(partial_url):
  url = SWYFTX_API_BASE + partial_url
  try:
    # Need to add browser headers
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    openurl = urllib.request.urlopen(req)
    return json.loads(openurl.read().decode('utf-8'))
  except Exception as ex:
    logging.error("Failed to send request to " + url)
    logging.error(ex)
    return None

class SwyftxApi:
  _coin_codes=[]
  _base_asset=""
  _resolution=""
  _side=""
  def __init__(self, base_asset="AUD", resolution="5m", side="bid"):
    self._base_asset = base_asset
    self._resolution = resolution
    self._side = side
    # populate coin codes to start
    basic_info = RequestApi(SWYFTX_BASIC_INFO)
    for coin_info in basic_info:
      self._coin_codes.append(coin_info["code"])

  def get_latest_bars(self):
    bars=[]
    for code in self._coin_codes:
      logging.info("Getting data for " + code)
      coin_data = RequestApi(SWYFTX_LATEST_BAR + self._base_asset + "/" + code + "/" + self._side + "/?resolution=" + self._resolution)
      if coin_data is None:
        logging.error("Failed to get coin data for " + code)
      else:
        bars.append(coin_data)

    return bars
