"""Secure CCXT adapter with paper-trade mode."""
import ccxt
import os




class CCXTAdapter:
def __init__(self, exchange_id: str = 'binance', test: bool = True):
self.test = test
self.exchange = getattr(ccxt, exchange_id)({
'apiKey': os.getenv('EXCHANGE_API_KEY'),
'secret': os.getenv('EXCHANGE_API_SECRET'),
'enableRateLimit': True,
})


def place_order(self, symbol: str, side: str, amount: float, price: float = None):
if self.test:
print(f"[PAPER TRADE] {side} {amount} {symbol} @{price}")
return {"status": "paper_trade"}
else:
return self.exchange.create_order(symbol, 'market', side, amount)
