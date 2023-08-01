import csv
from datetime import datetime
from typing import List
from pyport.security import Security
from pyport.transaction import Transaction


class TransactionManager:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_from_csv(self) -> List[Transaction]:
        transactions = []
        with open(self.file_path, 'r') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            for row in csv_reader:
                amount = float(row['amount'])
                security_name = row['security']
                date_str = row['date']

                date = datetime.strptime(date_str, '%Y-%m-%d')
                security = Security(name=security_name)
                transaction = Transaction(
                    amount=amount, security=security, date=date)

                transactions.append(transaction)
        return transactions
