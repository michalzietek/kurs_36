class OrderProcessor:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def process_order(self, product: str, quantity: int) -> bool:
        if self.inventory.check_availability(product, quantity):
            self.inventory.update_stock(product, quantity)
            return True
        return False
