import responses
import pytest

from coinbin import Coinbin, ApiError


@responses.activate
def test_request_exception():
    client = Coinbin()
    responses.add(responses.GET, 'https://coinbin.org/btc', body="err", status=500)
    with pytest.raises(ApiError):
        client.get_currency('btc')


@responses.activate
def test_get_currency():
    client = Coinbin()
    body = """
    {
      "coin": {
        "btc": 1.00000000,
        "name": "Bitcoin",
        "rank": 1,
        "ticker": "btc",
        "usd": 4592.25
      }
    }
    """
    responses.add(responses.GET, 'https://coinbin.org/btc', body=body, status=200)
    btc = client.get_currency('btc')
    assert btc.usd == 4592.25
    assert btc.name == 'Bitcoin'


@responses.activate
def test_get_currency_price():
    client = Coinbin()
    body = """
    {
      "coin": {
        "exchange_rate": 4584.39,
        "usd": 458439.00000000
      }
    }
    """
    responses.add(responses.GET, 'https://coinbin.org/btc/100', body=body, status=200)
    btc = client.get_currency_price('BTC', 100)
    assert btc.usd == 458439.00000000
    assert btc.exchange_rate == 4584.39


@responses.activate
def test_get_exchange_rate():
    client = Coinbin()
    body = """
    {
      "coin": {
        "exchange_rate": 0.07538434
      }
    }
    """
    responses.add(responses.GET, 'https://coinbin.org/eth/to/btc', body=body, status=200)
    eth = client.get_exchange_rate('ETH', 'BTC')
    assert eth.exchange_rate == 0.07538434


@responses.activate
def test_list_currencies():
    client = Coinbin()
    with open('tests/all_currencies.json') as f:
        body = f.read()

    responses.add(responses.GET, 'https://coinbin.org/coins', body=body, status=200)
    coins = client.list_currencies()
    assert coins['btc'].usd == 4583.18
