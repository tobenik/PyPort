import pytest
from datetime import datetime
from pyport import Portfolio, Security, Transaction

transaction_date = datetime(2023, 1, 1)
aapl = Security(name="AAPL")


def test_creating_portfolio():
    portfolio = Portfolio("MyPortfolio", cash_balance=500)
    assert portfolio.name == "MyPortfolio"
    assert portfolio.cash_balance == 500
    assert len(portfolio.transactions) == 0


def test_add_transaction():
    buy_transaction = Transaction(
        amount=2000, security=aapl, date=transaction_date)
    portfolio = Portfolio("MyPortfolio", cash_balance=500)

    portfolio.add_transaction(transaction=buy_transaction)
    assert len(portfolio.transactions) == 1
    assert portfolio.transactions[0].amount == 2000
    assert portfolio.transactions[0].security == aapl
    assert portfolio.transactions[0].date == transaction_date


def test_invalid_types_for_trasnaction():
    with pytest.raises(TypeError):
        Transaction(
            amount="ABC", security="null", date="invalid")
