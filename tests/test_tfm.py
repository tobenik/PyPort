import pytest
import csv
from datetime import date
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

data_path = "tests/testdata/transactions.csv"
ex_data = [
    {"date": date(2023, 1, 1), "security": "AAPL", "quantity": 20, "price": 100},
    {"date": date(2023, 1, 1), "security": "AMZN", "quantity": 100, "price": 23.67},
    {"date": date(2023, 2, 1), "security": "AAPL", "quantity": -10, "price": 34.53},
    {"date": date(2023, 2, 2), "security": "TSLA", "quantity": 30, "price": 0.42}]
headers = list(ex_data[0].keys())

### Start: Helper functions ###


def clearTestData():
    open(data_path, 'w').close()  # clear datafile


def populateTestData():
    with open(data_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ex_data)

### End: Helper Functions ###


def test_is_empty():
    clearTestData()
    tfm = TransactionFileManager(data_path)
    clearTestData()

    assert tfm.is_empty() == True


def test_with_empty_file():
    clearTestData()
    tfm = TransactionFileManager(data_path)

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert tfm.read_transactions() == []


def test_read_with_populated_file():
    clearTestData()
    populateTestData()
    tfm = TransactionFileManager(data_path)
    first_transaction = Transaction(*list(ex_data[0].values()))

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert tfm.read_transactions()[0].get_dict(
    ) == first_transaction.get_dict()


def test_add_with_empty_file():
    clearTestData()
    tfm = TransactionFileManager(data_path)
    t = Transaction(*list(ex_data[0].values()))
    tfm.add_transaction(t)

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert len(tfm.read_transactions()) == 1
    assert tfm.read_transactions()[0].get_dict() == t.get_dict()
