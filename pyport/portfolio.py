from typing import List
from pyport.transaction import Transaction


class Portfolio:
    def __init__(self, name: str, cash_balance: float = 0):
        self.name = name
        self.cash_balance = cash_balance
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.cash_balance -= transaction.amount
    
    def print_transactions(self):
        holdings = ""
        for t in self.transactions:
            holdings += f"{t.security.name}: {t.amount} | {t.date}"
        print(holdings)
