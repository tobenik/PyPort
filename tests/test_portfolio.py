import pytest
from datetime import date
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

tfm = None

def test_initalize_tfm() -> None:
    global tfm
    tfm = TransactionFileManager()

def clearTestData() -> None:
    tfm.clear_transactions()


def populateTestData() -> None:
    tfm.add_transaction(Transaction(date(2000, 1, 1), "AAPL", 250, 12.34))
    tfm.add_transaction(Transaction(date(2000, 1, 1), "AMZN", 520, 13.24))
    tfm.add_transaction(Transaction(date(2000, 3, 3), "AAPL", 205, 14.32))
    tfm.add_transaction(Transaction(date(2000, 4, 4), "MSFT", 502, 12.43))


def test_create_portfolio() -> None:
    clearTestData()
    cash = 500000
    p = Portfolio("Test", start_balance=cash)

    assert p.get_name() == "Test"
    assert len(p.get_transactions()) == 0
    assert p.get_balance() == cash

    clearTestData()


def test_add_transaction_to_empty() -> None:
    clearTestData()
    s = "AAPL"
    t = Transaction(date(2000, 1, 1), s, 250, 43.21)
    p = Portfolio("Test", start_balance=50000)

    p.add_transaction(t)

    assert len(p.get_transactions()) == 1
    assert p.get_transactions()[0].get_dict() == t.get_dict()
    assert p.get_balance() == 50000 - t.get_total()

    clearTestData()


def test_add_multiple_to_empty():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    transactions_to_add = [
        Transaction(date(2000, 1, 1), "AAPL", 50, 25.50),
        Transaction(date(2000, 1, 2), "AMZN", 30, 30.75),
        Transaction(date(2000, 1, 3), "MSFT", 20, 40.00)
    ]

    # Add multiple transactions at once
    for t in transactions_to_add:
        p.add_transaction(t)

    # Verify that all transactions were added and balance is updated correctly
    assert len(p.get_transactions()) == len(transactions_to_add)
    assert p.get_balance() == 1000 - sum(t.get_total()
                                         for t in transactions_to_add)

    clearTestData()


def test_add_transaction_to_existing() -> None:
    populateTestData()
    s = "TSLA"
    t = Transaction(date(2000, 1, 1), s, 250, 43.21)
    p = Portfolio("Test", start_balance=50000)

    # Check that data file was populated and p reads in transactions
    pre_transactions = len(p.get_transactions())
    pre_balance = p.get_balance()
    assert pre_transactions > 1

    p.add_transaction(t)

    assert len(p.get_transactions()) == pre_transactions + 1
    assert p.get_transactions()[-1].get_dict() == t.get_dict()
    assert p.get_balance() == pre_balance - t.get_total()

    clearTestData()


def test_fetch_transactions_after_adding_new_ones():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    transactions_to_add = [
        Transaction(date(2000, 1, 1), "AAPL", 50, 25.50),
        Transaction(date(2000, 1, 2), "AMZN", 30, 30.75),
        Transaction(date(2000, 1, 3), "MSFT", 20, 40.00)
    ]

    # Add multiple transactions at once
    for t in transactions_to_add:
        p.add_transaction(t)

    # Fetch transactions after adding new ones
    fetched_transactions = p.get_transactions()

    # Verify that the fetched transactions list is equal to the added transactions
    assert len(fetched_transactions) == len(transactions_to_add)
    for t1, t2 in zip(fetched_transactions, transactions_to_add):
        assert t1.get_dict() == t2.get_dict()

    clearTestData()


def test_add_sell_transaction():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t = Transaction(date(2000, 1, 1), "AAPL", -50, 25.50)

    p.add_transaction(t)

    assert len(p.get_transactions()) == 1
    assert p.get_balance() == 1000 - t.get_total()

    clearTestData()


def test_get_holdings_empty_portfolio():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    assert p.get_holdings() == {}

    clearTestData()


def test_get_holdings_single_security():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t1 = Transaction(date(2000, 1, 1), "AAPL", 50, 25.50)
    t2 = Transaction(date(2000, 1, 2), "AAPL", 30, 30.75)
    p.add_transaction(t1)
    p.add_transaction(t2)

    assert p.get_holdings() == {"AAPL": 50 + 30}

    clearTestData()


def test_get_holdings_multiple_securities():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t1 = Transaction(date(2000, 1, 1), "AAPL", 50, 25.50)
    t2 = Transaction(date(2000, 1, 2), "AMZN", 30, 30.75)
    t3 = Transaction(date(2000, 1, 3), "AAPL", 20, 40.00)
    p.add_transaction(t1)
    p.add_transaction(t2)
    p.add_transaction(t3)

    assert p.get_holdings() == {"AAPL": 50 + 20, "AMZN": 30}

    clearTestData()
