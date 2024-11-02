from typing import Optional

class Config:
    def __init__(self, currency_symbol: str = "PLN", buy_color: Optional[str] = None, sell_color: Optional[str] = None):
        self.currency_symbol = currency_symbol
        self.buy_color = buy_color
        self.sell_color = sell_color
