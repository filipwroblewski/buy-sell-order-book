from config import Config
from order import Order, OrderType, ActionType
from order_book import OrderBook

def main():
    config = Config(currency_symbol="PLN", buy_color="green", sell_color="red")
    order_book = OrderBook(config)

    orders_list = [
        Order("001", OrderType.BUY, ActionType.ADD, 20.00, 100),
        Order("002", OrderType.SELL, ActionType.ADD, 25.00, 200),
        Order("003", OrderType.BUY, ActionType.ADD, 23.00, 50),
        Order("004", OrderType.BUY, ActionType.ADD, 23.00, 70),
        Order("003", OrderType.BUY, ActionType.REMOVE, 23.00, 50),
        Order("005", OrderType.SELL, ActionType.ADD, 28.00, 100),
    ]

    for order in orders_list:
        (order_book.add_order if order.action == ActionType.ADD else order_book.remove_order)(order)

    order_book.display_best_prices()

if __name__ == "__main__":
    main()
