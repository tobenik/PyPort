import pytest
from datetime import date, datetime
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

tfm = None
example_transactions = [
    {
        "transactionDate": date(2000, 1, 1),
        "securityName": "AAPL",
        "quantity": 25,
        "price": 380.50
    },
    {
        "transactionDate": date(2001, 1, 1),
        "securityName": "AAPL",
        "quantity": 15,
        "price": 420.30
    },
    {
        "transactionDate": date(2001, 5, 14),
        "securityName": "MSFT",
        "quantity": 250,
        "price": 12.46
    },
    {
        "transactionDate": date(2002, 10, 11),
        "securityName": "TSLA",
        "quantity": 8,
        "price": 1095.50
    },
]


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
    p = Portfolio("Test", start_balance=50000)
    t = example_transactions[0]
    p.add_transaction(**t)

    assert len(p.get_transactions()) == 1
    assert p.get_transactions()[0].get_price() == t['price']
    assert p.get_transactions()[0].get_quantity() == t['quantity']
    assert p.get_transactions()[0].get_security() == t['securityName']
    assert p.get_transactions()[0].get_transaction_date() == datetime.strftime(t['transactionDate'], "%Y-%m-%d")
    assert p.get_balance() == 50000 - t['price'] * t['quantity']

    clearTestData()


def test_add_multiple_to_empty():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    # Add multiple transactions at once
    for t in example_transactions:
        p.add_transaction(**t)

    # Verify that all transactions were added and balance is updated correctly
    assert len(p.get_transactions()) == len(example_transactions)
    assert p.get_balance() == 1000 - sum(t['quantity'] * t['price']
                                         for t in example_transactions)

    clearTestData()


def test_add_transaction_to_existing() -> None:
    populateTestData()
    t = example_transactions[-1]
    p = Portfolio("Test", start_balance=50000)

    # Check that data file was populated and p reads in transactions
    pre_transactions = len(p.get_transactions())
    pre_balance = p.get_balance()
    assert pre_transactions > 1

    p.add_transaction(**t)

    assert len(p.get_transactions()) == pre_transactions + 1
    assert p.get_transactions()[-1].get_price() == t['price']
    assert p.get_transactions()[-1].get_quantity() == t['quantity']
    assert p.get_transactions()[-1].get_security() == t['securityName']
    assert p.get_transactions()[-1].get_transaction_date() == datetime.strftime(t['transactionDate'], "%Y-%m-%d")
    assert p.get_balance() == pre_balance - t['price'] * t['quantity']

    clearTestData()


def test_fetch_transactions_after_adding_new_ones():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    # Add multiple transactions at once
    for t in example_transactions:
        p.add_transaction(**t)

    # Fetch transactions after adding new ones
    fetched_transactions = p.get_transactions()

    # Verify that the fetched transactions list is equal to the added transactions
    assert len(fetched_transactions) == len(example_transactions)
    for t1, t2 in zip(fetched_transactions, example_transactions):
        assert t1.get_price() == t2['price']
        assert t1.get_quantity() == t2['quantity']
        assert t1.get_security() == t2['securityName']
        assert t1.get_transaction_date() == datetime.strftime(t2['transactionDate'], "%Y-%m-%d")

    clearTestData()


def test_add_sell_transaction():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t = example_transactions[1]

    p.add_transaction(**t)

    assert len(p.get_transactions()) == 1
    assert p.get_balance() == 1000 - t['price'] * t['quantity']

    clearTestData()


def test_get_holdings_empty_portfolio():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)

    assert p.get_holdings() == {}

    clearTestData()


def test_get_holdings_single_security():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t1 = {
        "transactionDate": date(2000, 1, 1),
        "securityName": "AAPL",
        "quantity": 50,
        "price": 25.50
    }
    t2 = {
        "transactionDate": date(2000, 1, 2),
        "securityName": "AAPL",
        "quantity": 30,
        "price": 20.75
    }

    p.add_transaction(**t1)
    p.add_transaction(**t2)

    assert p.get_holdings() == {"AAPL": t1['quantity'] + t2['quantity']}

    clearTestData()


def test_get_holdings_multiple_securities():
    clearTestData()
    p = Portfolio("Test", start_balance=1000)
    t1 = {
        "transactionDate": date(2000, 1, 1),
        "securityName": "AAPL",
        "quantity": 50,
        "price": 25.50
    }
    t2 = {
        "transactionDate": date(2000, 2, 1),
        "securityName": "AMZN",
        "quantity": 100,
        "price": 2.50
    }
    t3 = {
        "transactionDate": date(2000, 2, 1),
        "securityName": "AAPL",
        "quantity": 10,
        "price": 30.25
    }
    t4 = {
        "transactionDate": date(2000, 3, 21),
        "securityName": "AMZN",
        "quantity": 250,
        "price": 1.75
    }

    p.add_transaction(**t1)
    p.add_transaction(**t2)
    p.add_transaction(**t3)
    p.add_transaction(**t4)

    assert p.get_holdings() == {
        "AAPL": t1["quantity"] + t3["quantity"],
        "AMZN": t2["quantity"] + t4["quantity"]
    }

    clearTestData()
