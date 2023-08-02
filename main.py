from pyport.portfolio import Portfolio
from pyport.transaction_file_manager import TransactionFileManager


def main():
    tm = TransactionFileManager(file_path='data/ex_transactions.csv')
    portfolio = Portfolio("MyPortfolio", tm, start_balance=20000)
    portfolio.print_info()


if __name__ == "__main__":
    main()
