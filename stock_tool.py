# stock_tool.py
# Author: Nikita Lemeshenko


class StockLookup:
    """A tool that checks how many products are in stock."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        if product in self.stock:
            return self.stock[product]
        return None
