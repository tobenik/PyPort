from typing import Union
from datetime import datetime
from pyport.security import Security


class Transaction:
    def __init__(self, amount: Union[int, float], security: Security, date: datetime):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be of type int or float.")
        if not isinstance(security, Security):
            raise TypeError("security must be an instance of Security")
        if not isinstance(date, datetime):
            raise TypeError("date must be an instance of datetime")

        self.date = date
        self.security = security
        self.amount = amount
