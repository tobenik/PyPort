from typing import Union
from datetime import date, datetime


class Transaction:
    def __init__(self, trans_date: date, security: str, quantity: int, price: float):
        if not isinstance(quantity, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(price, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(security, str):
            raise TypeError("security must be of type string")
        if not isinstance(trans_date, date):
            raise TypeError("date must be an instance of datetime")

        self.__transaction_date = trans_date
        self.__security = security
        self.__quantity = int(quantity)
        self.__price = float(price)

    def get_transaction_date(self) -> str:
        return datetime.strftime(self.__transaction_date, '%Y-%m-%d')

    def get_security(self) -> str:
        return self.__security

    def get_quantity(self) -> int:
        return self.__quantity
    
    def get_price(self) -> float:
        return self.__price

    def get_total(self) -> float:
        return self.__quantity * self.__price

    def get_dict(self) -> dict[str, Union[int, str]]:
        return {
            "date": self.get_transaction_date(),
            "security": self.get_security(),
            "quantity": self.get_quantity(),
            "price": self.get_price()
        }
