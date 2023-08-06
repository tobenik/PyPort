from datetime import date
from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager
from pyport.portfolio_printer import PortfolioPrinter

def print_info(portfolio: Portfolio) -> None:
        def print_header(header: str) -> None:
            LINEWIDTH = 50
            SECTION_PATTERN = "-"
            filling = f"{(LINEWIDTH-len(header))//2 * SECTION_PATTERN}"
            section_header = f"{filling}{header}{filling}"
            print(f"{section_header}{'-' if len(section_header) % 2 == 1 else ''}")

        transactions_str = ""
        for t in portfolio.get_transactions():
            d = t.get_transaction_date()
            s = t.get_security()
            q = t.get_quantity()
            p = t.get_price()
            transactions_str += f"{s}\t|\t{q} at {p}€\t|\t{d}\n"
        print_header("BALANCE")
        print(portfolio.get_balance())
        print_header("TRANSACTIONS")
        print(transactions_str)


def main():
    portfolio = Portfolio("MyPortfolio", start_balance=100000)
    t = Transaction(date(2023, 5, 1), "AMZN", 95, 130.24)
    portfolio.add_transaction(t)
    pp = PortfolioPrinter(portfolio, linewidth=60)

    pp.balance()
    pp.holdings()
    pp.transactions()



if __name__ == "__main__":
    main()
