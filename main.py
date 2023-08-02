from datetime import datetime
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager


def main():
    tm = TransactionFileManager(file_path='data/ex_transactions.csv')
    portfolio = Portfolio("MyPortfolio", tm, start_balance=20000)
    # buy_aapl = Transaction(amount=15000, security=Security(
    #     "AAPL"), transaction_date=date(2023, 1, 1))
    # portfolio.add_transaction(transaction=buy_aapl)
    portfolio.print_info()


if __name__ == "__main__":
    main()
