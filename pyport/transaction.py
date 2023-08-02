from typing import Union
from datetime import date, datetime


class Transaction:
    def __init__(self, amount: Union[int, float], security: str, transaction_date: date):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(security, str):
            raise TypeError("security must be of type string")
        if not isinstance(transaction_date, date):
            raise TypeError("date must be an instance of datetime")

        self._transaction_date = transaction_date
        self._security = security
        self._amount = amount

    def get_dict(self) -> dict[str, Union[int, float, str, date]]:
        as_dict = {"date": datetime.strftime(self._transaction_date, '%Y-%m-%d'),
                   "security": self._security, "amount": self._amount}
        return as_dict
