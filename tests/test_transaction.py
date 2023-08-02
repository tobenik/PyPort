import pytest
from datetime import date, datetime
from pyport.transaction import Transaction


def test_create_transaction():
    amount = 100
    transaction_date = date(2000, 1, 1)
    security = "AAPL"
    t = Transaction(amount, security, transaction_date)

    assert t.get_transaction_date() == datetime.strftime(transaction_date, '%Y-%m-%d')
    assert t.get_amount() == amount
    assert t.get_security() == security


def test_wrong_types_raise():
    amounts = [1, 2, "invalid"]
    dates = [date(1990, 12, 12), "2012-01-01", date(2000, 1, 1)]
    securities = [123, "AAPL", "AAPL"]

    for a, s, d in zip(amounts, securities, dates):
        with pytest.raises(TypeError):
            Transaction(a, s, d)


def test_get_dict():
    amount = 100
    transaction_date = date(2000, 1, 1)
    security = "AAPL"
    t = Transaction(amount, security, transaction_date)

    expected = {"date": datetime.strftime(transaction_date, '%Y-%m-%d'),
                "security": security, "amount": amount}
    actual = t.get_dict()

    assert expected == actual
