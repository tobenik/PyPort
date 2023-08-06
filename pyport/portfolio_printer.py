from typing import List
from pyport.portfolio import Portfolio


class PortfolioPrinter:
    def __init__(self, portfolio: Portfolio, linewidth: int = 50):
        self.__portfolio = portfolio
        self.__linewidth = linewidth

    def __centeredLine(self, text: str, pattern: str = " ", width=None) -> str:
        t = str(text)
        lineWidth = width if width is not None else self.__linewidth
        fillingLength = lineWidth - len(t)
        leftFilling = f"{(fillingLength) // 2 * pattern}"
        rightFilling = leftFilling + f"{(len(t) % 2) * pattern}"
        return f"{leftFilling}{t}{rightFilling}"
    
    def __nColumns(self, data: List[str], sep = "|") -> str:
        colWidth = self.__linewidth // len(data) - 1
        row = ""
        for col in data:
            row += self.__centeredLine(col, width=colWidth) + sep
        return row[:-len(sep)]

    def balance(self) -> None:
        b = str(round(self.__portfolio.get_balance(), 2))
        print(self.__centeredLine(" BALANCE ", pattern="-"))
        print(self.__centeredLine(b))
    
    def transactions(self) -> None:
        print(self.__centeredLine(" TRANSACTIONS ", pattern="-"))
        print(self.__nColumns(["Date", "Symbol", "Quantity", "Price"], sep="*"))
        for t in self.__portfolio.get_transactions():
            print(self.__nColumns(list(t.get_dict().values())))
    
    def holdings(self) -> None:
        h = self.__portfolio.get_holdings()
        print(self.__centeredLine(" HOLDINGS ", pattern="-"))
        print(self.__nColumns(["Symbol", "Quantity"], sep=" "))
        for security, quantity in h.items():
            print(self.__nColumns([security, quantity], sep =" "))


