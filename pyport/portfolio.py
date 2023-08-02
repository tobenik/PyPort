from typing import List
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager


class Portfolio:
    def __init__(self, name: str, transaction_file_manager: TransactionFileManager, start_balance: float = 0):
        self.__name = name
        self.__tfm = transaction_file_manager
        self.__start_balance = start_balance
        self.__transactions: List[Transaction] = self.__fetch_transactions()
        self.__current_balance = self.__compute_balance()

    def __fetch_transactions(self):
        return self.__tfm.read_transactions()

    def __compute_balance(self):
        balance = self.__start_balance
        for t in self.__transactions:
            balance -= t.get_total()
        return balance
    
    def get_name(self) -> str:
        return self.__name

    def get_balance(self) -> float:
        return self.__current_balance
    
    def get_transactions(self) -> List[Transaction]:
        return [t for t in self.__transactions]

    def add_transaction(self, transaction: Transaction) -> None:
        self.__transactions.append(transaction)
        self.__current_balance -= transaction.get_total()
        self.__tfm.add_transaction(transaction=transaction)
