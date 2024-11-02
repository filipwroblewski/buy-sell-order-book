from dataclasses import dataclass
from enum import Enum

class OrderType(Enum):
    BUY = "Buy"
    SELL = "Sell"

class ActionType(Enum):
    ADD = "Add"
    REMOVE = "Remove"

@dataclass
class Order:
    order_id: str
    order_type: OrderType
    action: ActionType
    price: float
    quantity: int
