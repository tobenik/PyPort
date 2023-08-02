import csv
import os
from datetime import datetime
from typing import List
from pyport.transaction import Transaction


class TransactionFileManager:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.headers: List[str] = ["date", "security", "quantity", "price"]
        self.initialize_file()

    def initialize_file(self):
        if self.is_empty():
            with open(self.file_path, 'a') as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=self.headers)
                writer.writeheader()

    def is_empty(self):
        return os.stat(self.file_path).st_size == 0

    def clear_transactions(self) -> None:
        open(self.file_path, 'w').close()
        self.initialize_file()

    def read_transactions(self) -> List[Transaction]:
        transactions = []
        with open(self.file_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                t_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                t_security = row['security']
                t_quantity = int(row['quantity'])
                t_price = float(row['price'])

                transaction = Transaction(t_date, t_security, t_quantity, t_price)
                transactions.append(transaction)

        return transactions

    def add_transaction(self, transaction: Transaction) -> None:
        with open(self.file_path, 'a') as csvFile:
            writer=csv.DictWriter(csvFile, fieldnames = self.headers)
            transaction_dict=transaction.get_dict()
            writer.writerow(transaction_dict)
