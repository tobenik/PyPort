import pytest
from datetime import date
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

data_path = "tests/testdata/transactions.csv"
tfm = TransactionFileManager(file_path=data_path)


def clearTestData() -> None:
    tfm.clear_transactions()


def populateTestData() -> None:
    tfm.add_transaction(Transaction(
        25000, "AAPL", date(2000, 1, 1)))
    tfm.add_transaction(Transaction(
        25000, "AAPL", date(2000, 2, 2)))
    tfm.add_transaction(Transaction(
        25000, "AMZN", date(2000, 3, 3)))
    tfm.add_transaction(Transaction(
        25000, "MSFT", date(2000, 4, 4)))


def test_create_portfolio() -> None:
    clearTestData()
    cash = 500000
    p = Portfolio("Test", tfm, start_balance=cash)

    assert p.get_name() == "Test"
    assert len(p.get_transactions()) == 0
    assert p.get_balance() == cash

    clearTestData()


def test_add_transaction_to_empty() -> None:
    clearTestData()
    s = "AAPL"
    t = Transaction(25000, s, date(2000, 1, 1))
    p = Portfolio("Test", tfm, start_balance=50000)

    p.add_transaction(t)

    assert len(p.get_transactions()) == 1
    assert p.get_transactions()[0] == t.get_dict()
    assert p.get_balance() == 50000 - t.get_dict()["amount"]

    clearTestData()


def test_add_transaction_to_existing() -> None:
    populateTestData()
    s = "TSLA"
    t = Transaction(2500, s, date(2000, 5, 5))
    p = Portfolio("Test", tfm, start_balance=50000)

    # Check that data file was populated and p reads in transactions
    pre_transactions = len(p.get_transactions())
    pre_balance = p.get_balance()
    assert pre_transactions > 1

    p.add_transaction(t)

    assert len(p.get_transactions()) == pre_transactions + 1
    assert p.get_transactions()[-1] == t.get_dict()
    assert p.get_balance() == pre_balance - t.get_dict()["amount"]

    clearTestData()
