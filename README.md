# buy-sell-order-book

Simulate basic stock exchange order book. Manage:
- Buy and sell orders, 
- Add and remove orders,
- Display best avaliable prices for buy and sell orders.

## Features

- Add and remove buy/sell orders (by prices and quantities)
- Track and display the best (highest bid/lowest ask) prices for each type of order
- Customizable currency symbol and display colors for buy/sell orders

## Requirements

1. Python 3.13
2. [requirements.txt](./requirements.txt)
   - Create and run `venv`
     - On Windows
       ```
       python -m venv venv
       venv/Scripts/activate
       ```

     - On Linux

       ```
       python3 -m venv venv
       . venv/bin/activate
       ```

   - Install requirements
    ```
    pip install -r requirements.txt
    ``` 

## Usage

```
python main.py
```
### Example Output

```txt
Added order 001: 100 at 20.0 PLN

Current Best Prices:
Best Buy Price: 20.0 PLN (Quantity: 100)
=========================
Added order 002: 200 at 25.0 PLN

Current Best Prices:
Best Buy Price: 20.0 PLN (Quantity: 100)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================
Added order 003: 50 at 23.0 PLN

Current Best Prices:
Best Buy Price: 23.0 PLN (Quantity: 50)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================
Added order 004: 70 at 23.0 PLN

Current Best Prices:
Best Buy Price: 23.0 PLN (Quantity: 120)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================
Removed 50 from order 003: Remaining quantity is 0
Order 003 has been removed

Current Best Prices:
Best Buy Price: 23.0 PLN (Quantity: 70)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================
Added order 005: 100 at 28.0 PLN

Current Best Prices:
Best Buy Price: 23.0 PLN (Quantity: 70)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================

Current Best Prices:
Best Buy Price: 23.0 PLN (Quantity: 70)
Best Sell Price: 25.0 PLN (Quantity: 200)
=========================
```
