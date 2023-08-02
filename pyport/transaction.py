from typing import Union
from datetime import datetime


class Transaction:
    def __init__(self, amount: Union[int, float], security: str, date: datetime):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(security, str):
            raise TypeError("security must be of type string")
        if not isinstance(date, datetime):
            raise TypeError("date must be an instance of datetime")

        self.date = date
        self.security = security
        self.amount = amount

    def get_dict(self) -> dict[str, Union[int, float, str, datetime]]:
        as_dict = {"date": self.date,
                   "security": self.security, "amount": self.amount}
        return as_dict
