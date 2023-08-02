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
            balance -= t.get_dict()["amount"]
        return balance

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.current_balance -= transaction.get_dict()["amount"]
        self.tfm.add_transaction(transaction=transaction)

    def print_info(self) -> None:
        def print_header(header: str) -> None:
            LINEWIDTH = 50
            SECTION_PATTERN = "-"
            filling = f"{(LINEWIDTH-len(header))//2 * SECTION_PATTERN}"
            section_header = f"{filling}{header}{filling}"
            print(f"{section_header}{'-' if len(section_header) % 2 == 1 else ''}")

        transactions_str = ""
        for t in self.transactions:
            t_dict = t.get_dict()
            s = t_dict["security"]
            a = t_dict["amount"]
            d = t_dict["date"]
            transactions_str += f"{s}\t|\t{a}\t|\t{d}\n"
        print_header("BALANCE")
        print(self.current_balance)
        print_header("TRANSACTIONS")
        print(transactions_str)
