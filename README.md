[![Build Status](https://travis-ci.org/adilkhash/pycoinbin.svg?branch=master)](https://travis-ci.org/adilkhash/pycoinbin)

# Python wrapper for coinbin.org

Simple wrapper around coinbin.org to retrieve information about cryptocurrencies

## Install

`pip install pycoinbin`

## Usage

You have to import Coinbin class from coinbin package and go ahead.

```python
>>> from coinbin import Coinbin
>>> client = Coinbin()
>>>
```

If you want to know more about particular cryptocurrency use `get_currency` method:

```python
>>> btc = client.get_currency('btc')
>>> print(btc.name, btc.rank, btc.usd)
Bitcoin 1 4584.94
>>> 
```

If you want to know how much costs particular amount of cryptocurrency then go ahead with `get_currency_price` method

```python
>>> btc = client.get_currency_price('btc', 100)
>>> print(btc.usd, btc.exchange_rate)
458494.0 4584.94
>>> 
```

Exchange rate between two cryptocurrencies can be obtained with `get_exchange_rate`

```python
>>> rate = client.get_exchange_rate('BTC', 'ETH')
>>> print(rate)
ExchangeRate(exchange_rate=13.24225487)
>>> 
```

List all available cryptocoins:

```python
>>> coins = client.list_currencies()
>>> print(coins)
{'$$$': Coin(btc=4.9e-07, name='Money', rank=334, ticker='$$$', usd=0.002257), '
>>>
```

History of particular coin can be retrieved by `get_currency_history`

```python
>>> btc = client.get_currency_history('btc')
```
