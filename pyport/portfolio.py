from typing import List
from pyport.transaction import Transaction
from pyport.transaction_manager import TransactionManager


class Portfolio:
    def __init__(self, name: str, transaction_manager: TransactionManager, starting_balance: float = 0):
        self.name = name
        self.start_balance = starting_balance
        self.current_balance = starting_balance
        self.transactions: List[Transaction] = []
        self.tm = transaction_manager

    def refresh(self):
        self.fetch_transactions()
        self.count_balance()

    def fetch_transactions(self):
        self.transactions = self.tm.read_from_csv()
    
    def count_balance(self):
        balance = self.start_balance
        for t in self.transactions:
            balance -= t.amount
        self.current_balance = balance

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.current_balance -= transaction.amount

    def print_info(self):
        separator = "\n- * - * - * - *\n"
        holdings = ""
        for t in self.transactions:
            holdings += f"{t.security.name}: {t.amount} | {t.date} \n"
        print("HOLDINGS", holdings, sep=separator)
        print("BALANCE", self.current_balance, sep=separator)
