# my_tool.py
# Author: Nikita Lemeshenko


class RepairPriceTool:
    """Stores prices for common bike repairs."""

    def __init__(self, prices):
        self.prices = prices

    def find_service(self, text):
        for service in self.prices:
            if service in text.lower():
                return service
        return None

    def price_for(self, service):
        return self.prices.get(service)
