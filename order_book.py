from collections import defaultdict
from typing import List, Dict, Optional
from termcolor import colored
from config import Config
from order import Order, OrderType
from exceptions import OrderNotFoundError, InsufficientQuantityError

class OrderBook:
    def __init__(self, config: Config):
        self.buy_orders: Dict[float, List[Order]] = defaultdict(list)
        self.sell_orders: Dict[float, List[Order]] = defaultdict(list)
        self.config = config

    def add_order(self, order: Order):
        try:
            orders = self.get_orders(order.order_type)
            existing_order = self.find_order(orders[order.price], order.order_id)

            if existing_order:
                existing_order.quantity += order.quantity
                print(f"Updated order {order.order_id}: New quantity is {existing_order.quantity}")
            else:
                orders[order.price].append(order)
                print(f"Added order {order.order_id}: {order.quantity} at {order.price} {self.config.currency_symbol}")

            self.display_best_prices()
        except Exception as e:
            print(f"Error when adding order: {e}")

    def remove_order(self, order: Order):
        try:
            orders = self.get_orders(order.order_type)
            existing_order = self.find_order(orders[order.price], order.order_id)

            if existing_order:
                if existing_order.quantity < order.quantity:
                    raise InsufficientQuantityError(
                        f"Cannot remove {order.quantity} from order {existing_order.order_id}: only {existing_order.quantity} available."
                    )
                
                existing_order.quantity -= order.quantity
                message = f"Removed {order.quantity} from order {existing_order.order_id}: Remaining quantity is {existing_order.quantity}"
                print(message)

                if existing_order.quantity <= 0:
                    print(f"Order {existing_order.order_id} has been removed")
                    orders[order.price].remove(existing_order)

                if not orders[order.price]:
                    del orders[order.price]
            else:
                raise OrderNotFoundError(f"Order {order.order_id} not found for remove operation.")

            self.display_best_prices()
        except (OrderNotFoundError, InsufficientQuantityError) as e:
            print(f"Error while removing order: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_best_prices(self):
        best_buy_price = max(self.buy_orders.keys(), default=None)
        best_sell_price = min(self.sell_orders.keys(), default=None)

        print("\nCurrent Best Prices:")
        messages = []
        if best_buy_price:
            messages.append(self.format_price_display(best_buy_price, self.buy_orders, self.config.buy_color, "Best Buy Price"))
        if best_sell_price:
            messages.append(self.format_price_display(best_sell_price, self.sell_orders, self.config.sell_color, "Best Sell Price"))

        print("\n".join(messages))
        print("=" * 25)

    def get_orders(self, order_type: OrderType) -> Dict[float, List[Order]]:
        return self.buy_orders if order_type == OrderType.BUY else self.sell_orders

    def find_order(self, orders: List[Order], order_id: str) -> Optional[Order]:
        return next((o for o in orders if o.order_id == order_id), None)

    def format_price_display(self, price: float, orders: Dict[float, List[Order]], color: Optional[str], label: str) -> str:
        quantity = sum(order.quantity for order in orders[price])
        price_display = f"{label}: {price} {self.config.currency_symbol} (Quantity: {quantity})"
        return colored(price_display, color) if color else price_display
