from pyport.portfolio import Portfolio
from pyport.transaction import Transaction
from pyport.transaction_file_manager import TransactionFileManager

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
    tm = TransactionFileManager(file_path='data/ex_transactions.csv')
    portfolio = Portfolio("MyPortfolio", tm, start_balance=20000)
    print_info(portfolio)


if __name__ == "__main__":
    main()
