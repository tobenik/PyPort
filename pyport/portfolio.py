from typing import List
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager


class Portfolio:
    def __init__(self, name: str, start_balance: float = 0):
        self.name = name
        self.start_balance = start_balance
        self.tfm = TransactionFileManager()
        self.transactions: List[Transaction] = self.__fetch_transactions()
        self.current_balance = self.__compute_balance()

    def __fetch_transactions(self):
        return self.tfm.read_transactions()

    def __compute_balance(self):
        balance = self.start_balance
        for t in self.transactions:
            balance -= t.get_total()
        return balance

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.current_balance -= transaction.get_total()
        self.tfm.add_transaction(transaction=transaction)

    def get_name(self) -> str:
        return self.name

    def get_balance(self) -> float:
        return self.current_balance

    def get_transactions(self) -> List[Transaction]:
        return self.transactions

    def get_holdings(self) -> dict[str, int]:
        holdings = {}
        for t in self.get_transactions():
            s = t.get_security()
            if s in holdings:
                holdings[s] += t.get_quantity()
            else:
                holdings[s] = t.get_quantity()
        return holdings