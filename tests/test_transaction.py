import pytest
from datetime import date, datetime
from pyport.transaction import Transaction


def test_create_transaction():
    quantity = 100
    price = 15.20
    transaction_date = date(2000, 1, 1)
    security = "AAPL"
    t = Transaction(transaction_date, security, quantity, price)

    assert t.get_transaction_date() == datetime.strftime(transaction_date, '%Y-%m-%d')
    assert t.get_security() == security
    assert t.get_quantity() == quantity
    assert t.get_price() == price


def test_wrong_types_raise():
    dates = ["2012-01-01",date(1990, 12, 12), 
             date(2000, 1, 1), date(2020, 5, 5)]
    securities = ["AAPL", 123, "MSFT", "AMZN"]
    quantities = [100, 25, "invalid", -45]
    prices = [19.24, 12, 97.00, "high"]

    for d, s, q, p in zip(dates, securities, quantities, prices):
        with pytest.raises(TypeError):
            Transaction(d, s, q, p)


def test_get_dict():
    transaction_date = date(2000, 1, 1)
    security = "AAPL"
    quantity = 100
    price = 12.34
    t = Transaction(transaction_date, security, quantity, price)

    expected = {"date": datetime.strftime(transaction_date, '%Y-%m-%d'),
                "security": security, "quantity": quantity, "price": price}
    actual = t.get_dict()

    assert expected == actual

def test_get_total():
    quantity = 100
    price = 15.20
    transaction_date = date(2000, 1, 1)
    security = "AAPL"
    t = Transaction(transaction_date, security, quantity, price)

    expected_total = quantity * price
    assert t.get_total() == expected_total

def test_invalid_date_format_raises():
    invalid_date_format = "2022/01/01"
    security = "AAPL"
    quantity = 100
    price = 12.34

    with pytest.raises(TypeError):
        Transaction(invalid_date_format, security, quantity, price)
