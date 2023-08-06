from typing import Union
from datetime import date, datetime


class Transaction:
    def __init__(self, transactionDate: date, securityName: str, quantity: int, price: float):
        if not isinstance(quantity, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(price, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(securityName, str):
            raise TypeError("security must be of type string")
        if not isinstance(transactionDate, date):
            raise TypeError("date must be an instance of datetime")

        self.transactionDate = transactionDate
        self.securityName = securityName
        self.quantity = int(quantity)
        self.price = float(price)

    def get_transaction_date(self) -> str:
        return datetime.strftime(self.transactionDate, '%Y-%m-%d')

    def get_security(self) -> str:
        return self.securityName

    def get_quantity(self) -> int:
        return self.quantity
    
    def get_price(self) -> float:
        return self.price

    def get_total(self) -> float:
        return self.quantity * self.price

    def get_dict(self) -> dict[str, Union[int, str]]:
        return {
            "date": self.get_transaction_date(),
            "security": self.get_security(),
            "quantity": self.get_quantity(),
            "price": self.get_price()
        }
