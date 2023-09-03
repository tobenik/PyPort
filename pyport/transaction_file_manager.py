import csv
import os
from datetime import datetime
from typing import List
import configparser
from pyport.transaction import Transaction


class TransactionFileManager:
    def __init__(self) -> None:
        self.file_path = self.__get_filepath()
        self.headers: List[str] = ["date", "security", "quantity", "price"]
        self.initialize_file()
    
    def __get_filepath(self) -> str:
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        test_mode = os.environ.get('PYPORT_TEST_MODE', "False")
        
        if test_mode.lower() == 'true':
            return config['datapaths']['test_transactions']
        
        return config['datapaths']['transactions']

    def initialize_file(self) -> None:
        #if self.is_empty(): // Restart file every time
        with open(self.file_path, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.headers)
            writer.writeheader()

    def is_empty(self) -> bool:
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
