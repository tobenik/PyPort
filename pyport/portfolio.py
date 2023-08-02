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
            balance -= t.get_dict()["amount"]
        return balance
    
    def get_name(self) -> str:
        return self.__name

    def get_balance(self) -> float:
        return self.__current_balance
    
    def get_transactions(self):
        return [t.get_dict() for t in self.__transactions]

    def add_transaction(self, transaction: Transaction) -> None:
        self.__transactions.append(transaction)
        self.__current_balance -= transaction.get_dict()["amount"]
        self.__tfm.add_transaction(transaction=transaction)

    def print_info(self) -> None:
        def print_header(header: str) -> None:
            LINEWIDTH = 50
            SECTION_PATTERN = "-"
            filling = f"{(LINEWIDTH-len(header))//2 * SECTION_PATTERN}"
            section_header = f"{filling}{header}{filling}"
            print(f"{section_header}{'-' if len(section_header) % 2 == 1 else ''}")

        transactions_str = ""
        for t in self.__transactions:
            t_dict = t.get_dict()
            s = t_dict["security"]
            a = t_dict["amount"]
            d = t_dict["date"]
            transactions_str += f"{s}\t|\t{a}\t|\t{d}\n"
        print_header("BALANCE")
        print(self.get_balance())
        print_header("TRANSACTIONS")
        print(transactions_str)
