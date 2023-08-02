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

        self.__transaction_date = transaction_date
        self.__security = security
        self.__amount = amount

    def get_dict(self) -> dict[str, Union[int, float, str, date]]:
        as_dict = {"date": datetime.strftime(self.__transaction_date, '%Y-%m-%d'),
                   "security": self.__security, "amount": self.__amount}
        return as_dict
