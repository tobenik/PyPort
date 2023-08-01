from typing import List, Union
from datetime import datetime


class Security:
    def __init__(self, name: str):
        self.name = name


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


class Portfolio:
    def __init__(self, name: str, cash_balance: float = 0):
        self.name = name
        self.cash_balance = cash_balance
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
