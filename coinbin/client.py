from __future__ import print_function
import logging
from collections import namedtuple

import requests

logger = logging.getLogger(__name__)

CURRENCY_ENDPOINT = 'https://coinbin.org/{currency_code}'
CURRENCY_PRICE_ENDPOINT = 'https://coinbin.org/{currency_code}/{currency_amount}'
CURRENCY_EXCHANGE_RATE_ENDPOINT = 'https://coinbin.org/{from_currency_code}/to/{to_currency_code}'
CURRENCY_HISTORY_ENDPOINT = 'https://coinbin.org/{currency_code}/history'


Coin = namedtuple('Coin', 'btc name rank ticker usd')
CoinPrice = namedtuple('CoinPrice', 'exchange_rate usd')
ExchangeRate = namedtuple('ExchangeRate', 'exchange_rate')


class ApiError(Exception):
    pass


class Coinbin(object):
    def _get(self, endpoint):
        try:
            response = requests.get(endpoint, timeout=(10, 15))
            response.raise_for_status()
        except requests.RequestException as e:
            logger.exception(e)
            raise ApiError(e)
        else:
            return response.json()

    def _tuplify(self, _tuple_class, payload):
        args = {field: payload['coin'].get(field)
                for field in _tuple_class.__dict__['_fields'] if field in payload['coin']}
        if args:
            return _tuple_class(**args)

    def get_currency(self, currency_code):
        url = CURRENCY_ENDPOINT.format(currency_code=currency_code.lower())
        payload = self._get(url)
        return self._tuplify(Coin, payload)

    def get_currency_price(self, currency_code, currency_amount):
        url = CURRENCY_PRICE_ENDPOINT.format(currency_code=currency_code.lower(),
                                             currency_amount=currency_amount)
        payload = self._get(url)
        return self._tuplify(CoinPrice, payload)

    def get_exchange_rate(self, from_currency_code, to_currency_code):
        url = CURRENCY_EXCHANGE_RATE_ENDPOINT.format(from_currency_code=from_currency_code.lower(),
                                                     to_currency_code=to_currency_code.lower())
        payload = self._get(url)
        return self._tuplify(ExchangeRate, payload)

    def get_currency_history(self, currency_code):
        url = CURRENCY_HISTORY_ENDPOINT.format(currency_code=currency_code.lower())
        payload = self._get(url)
        return payload

    def list_currencies(self):
        response = self._get('https://coinbin.org/coins')
        coins = response['coins']
        payload = {k: Coin(**v) for k, v in coins.items()}
        return payload
