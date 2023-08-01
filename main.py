from datetime import datetime
from pyport.portfolio import Portfolio
from pyport.security import Security
from pyport.transaction import Transaction
from pyport.transaction_manager import TransactionManager


def main():
    tm = TransactionManager(file_path='transactions.csv')
    portfolio = Portfolio(name='My Portfolio', cash_balance=20000)
    buy_aapl = Transaction(amount=15000, security=Security(
        "AAPL"), date=datetime(2023, 1, 1))
    portfolio.add_transaction(transaction=buy_aapl)
    print("Portfolio cash balance: ", portfolio.cash_balance)
    portfolio.print_transactions()


if __name__ == "__main__":
    main()
