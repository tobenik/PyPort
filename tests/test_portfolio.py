from datetime import datetime
import pytest
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

data_path = "tests/testdata/transactions.csv"
tfm = TransactionFileManager(file_path=data_path)


def clearTestData() -> None:
    tfm.clear_transactions()


def populateTestData() -> None:
    tfm.add_transaction(Transaction(
        25000, "AAPL", datetime(2000, 1, 1)))
    tfm.add_transaction(Transaction(
        25000, "AAPL", datetime(2000, 2, 2)))
    tfm.add_transaction(Transaction(
        25000, "AMZN", datetime(2000, 3, 3)))
    tfm.add_transaction(Transaction(
        25000, "MSFT", datetime(2000, 4, 4)))


def test_create_portfolio() -> None:
    clearTestData()
    p = Portfolio("Test", tfm, start_balance=50000)

    assert p.name == "Test"
    assert p.start_balance == 50000
    assert len(p.transactions) == 0
    assert p.current_balance == p.start_balance

    clearTestData()


def test_add_transaction_to_empty() -> None:
    clearTestData()
    s = "AAPL"
    t = Transaction(25000, s, datetime(2000, 1, 1))
    p = Portfolio("Test", tfm, start_balance=50000)

    p.add_transaction(t)

    assert len(p.transactions) == 1
    assert p.transactions[0] == t
    assert p.current_balance == 50000 - t.amount
    assert p.start_balance == 50000

    clearTestData()


def test_add_transaction_to_existing() -> None:
    populateTestData()
    s = "TSLA"
    t = Transaction(2500, s, datetime(2000, 5, 5))
    p = Portfolio("Test", tfm, start_balance=50000)

    # Check that data file was populated and p reads in transactions
    pre_transactions = len(p.transactions)
    pre_balance = p.current_balance
    assert pre_transactions > 1

    p.add_transaction(t)

    assert len(p.transactions) == pre_transactions + 1
    assert p.transactions[-1] == t
    assert p.current_balance == pre_balance - t.amount
    assert p.start_balance == 50000

    clearTestData()
