# Python wrapper for coinbin.org

Simple wrapper around coinbin.org to retrieve information about cryptocurrencies

## Install

`pip install pycoinbin`

## Usage

```python
from coinbin import Coinbin
client = Coinbin()
bitcoin = client.get_currency_price('btc')
print(bitcoin.usd, bitcoin.name)
```