from datetime import datetime
import pytest
from pyport.security import Security
from pyport.transaction import Transaction


def test_create_transaction():
    amount = 100
    date = datetime(2000, 1, 1)
    security = Security("AAPL")
    t = Transaction(amount=amount, security=security, date=date)

    assert t.amount == amount
    assert t.date == date
    assert t.security == security


def test_wrong_types_raise():
    amounts = [1, 2, "invalid"]
    dates = [datetime(1990, 12, 12), "2012-01-01", datetime(2000, 1, 1)]
    securities = ["invalid", Security("AAPL"), Security("AAPL")]

    for a, d, s in zip(amounts, dates, securities):
        with pytest.raises(TypeError):
            Transaction(amount=a, security=s, date=d)


def test_get_dict():
    amount = 100
    date = datetime(2000, 1, 1)
    security = Security("AAPL")
    t = Transaction(amount=amount, security=security, date=date)

    expected = {"date": date, "name": security.name, "amount": amount}
    actual = t.get_dict()

    assert expected == actual
