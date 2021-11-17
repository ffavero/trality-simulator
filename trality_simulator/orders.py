"""Implement Trality order types.
"""

from enum import Enum


class OrderStatus(Enum):
    Created = 1
    Pending = 2
    PartiallyFilled = 3
    Filled = 4
    Canceled = 5
    Rejected = 6
    Expired = 7
    Error = 8
    BarrierTouched = 9
    StopTriggered = 10
    ForeignFilled = 11
    Unknown = 999


class OrderSide(Enum):
    Buy = 0
    Sell = 1


def order_market_value(symbol, value):
    """Sends a simple market order converting value in quoted currency
         to units of base currency.

    Args:
        symbol (string): The symbol to buy or sell.
        value (string or float): The desired value to buy or sell denoted
          in quoted currency. Negative values result in a sell order, while
          positive values result in a buy order.
    """
    pass


def order_market_amount(symbol, amount):
    pass


def order_trailing_iftouched_value(symbol, value, trailing_percent, stop_price):
    pass


def cancel_order(order_id):
    pass


def close_position(symbol):
    pass
