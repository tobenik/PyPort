from datetime import datetime
from pyport.portfolio import Portfolio
from pyport.security import Security
from pyport.transaction import Transaction
from pyport.transaction_manager import TransactionManager


def main():
    tm = TransactionManager(file_path='data/ex_transactions.csv')
    portfolio = Portfolio("MyPortfolio", tm, start_balance=20000)
    # buy_aapl = Transaction(amount=15000, security=Security(
    #     "AAPL"), date=datetime(2023, 1, 1))
    # portfolio.add_transaction(transaction=buy_aapl)
    portfolio.refresh()
    portfolio.print_info()


if __name__ == "__main__":
    main()
