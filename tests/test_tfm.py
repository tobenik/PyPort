import configparser
import pytest
import csv
from datetime import date
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

ex_data = [
    {"date": date(2023, 1, 1), "security": "AAPL",
     "quantity": 20, "price": 100},
    {"date": date(2023, 1, 1), "security": "AMZN",
     "quantity": 100, "price": 23.67},
    {"date": date(2023, 2, 1), "security": "AAPL",
     "quantity": -10, "price": 34.53},
    {"date": date(2023, 2, 2), "security": "TSLA", "quantity": 30, "price": 0.42}]
headers = list(ex_data[0].keys())

### Start: Helper functions ###

config = configparser.ConfigParser()
config.read('config/config.ini')
data_path = config['datapaths']['test_transactions']

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
    tfm = TransactionFileManager()
    clearTestData()

    assert tfm.is_empty() == True


def test_with_empty_file():
    clearTestData()
    tfm = TransactionFileManager()

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert tfm.read_transactions() == []


def test_read_with_populated_file():
    clearTestData()
    populateTestData()
    tfm = TransactionFileManager()
    first_transaction = Transaction(*list(ex_data[0].values()))

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert tfm.read_transactions()[0].get_dict(
    ) == first_transaction.get_dict()


def test_add_with_empty_file():
    clearTestData()
    tfm = TransactionFileManager()
    t = Transaction(*list(ex_data[0].values()))
    tfm.add_transaction(t)

    assert tfm.file_path == data_path
    assert tfm.headers == headers
    assert len(tfm.read_transactions()) == 1
    assert tfm.read_transactions()[0].get_dict() == t.get_dict()


def test_add_with_populated_file():
    clearTestData()
    populateTestData()
    tfm = TransactionFileManager()
    initial_transactions = tfm.read_transactions()

    t = Transaction(*list(ex_data[1].values()))
    tfm.add_transaction(t)

    updated_transactions = tfm.read_transactions()
    assert len(updated_transactions) == len(initial_transactions) + 1
    assert updated_transactions[-1].get_dict() == t.get_dict()


def test_clear_transactions():
    populateTestData()
    tfm = TransactionFileManager()

    # Verify file is not empty before clearing
    assert tfm.is_empty() is False

    tfm.clear_transactions()

    assert tfm.read_transactions() == []

    # Verify the file is reinitialized with headers
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        assert next(reader) == headers
