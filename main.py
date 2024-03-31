from datetime import date
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager
from pyport.portfolio_printer import PortfolioPrinter

def main():
    portfolio = Portfolio("MyPortfolio", start_balance=100000)
    pp = PortfolioPrinter(portfolio, linewidth=60)

    # Beginning state:
    print("--Beginning--")
    pp.balance()
    pp.holdings()
    pp.transactions()

    # Add BUY
    portfolio.add_transaction(date(2023, 5, 1), "AMZN", 95, 130.24)
    print("--Bought AMZN--")
    pp.balance()
    pp.holdings()
    pp.transactions()




if __name__ == "__main__":
    main()
