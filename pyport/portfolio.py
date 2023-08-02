from typing import List
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager


class Portfolio:
    def __init__(self, name: str, transaction_file_manager: TransactionFileManager, start_balance: float = 0):
        self.name = name
        self.tfm = transaction_file_manager
        self.start_balance = start_balance
        self.transactions: List[Transaction] = self.fetch_transactions()
        self.current_balance = self.compute_balance()

    def fetch_transactions(self):
        return self.tfm.read_transactions()

    def compute_balance(self):
        balance = self.start_balance
        for t in self.transactions:
            balance -= t.amount
        return balance

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.current_balance -= transaction.amount
        self.tfm.add_transaction(transaction=transaction)

    def print_info(self):
        separator = "\n- * - * - * - *\n"
        holdings = ""
        for t in self.transactions:
            holdings += f"{t.security.name}: {t.amount} | {t.date} \n"
        print("HOLDINGS", holdings, sep=separator)
        print("BALANCE", self.current_balance, sep=separator)
