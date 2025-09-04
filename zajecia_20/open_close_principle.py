from abc import ABC, abstractmethod


class DiscountCalculator:
    def calculate_discount(self, price: float, discount_type: str) -> float:
        if discount_type == "percentage":
            return price * 0.15
        elif discount_type == "newsletter":
            return 20
        elif discount_type == "vip":
            return price * 0.20
        elif discount_type == "boze_narodzenie":
            return discount_type * 0.24


class DiscountStrategy(ABC):
    @abstractmethod
    def calulate_discount(self, price: float) -> float:
        pass

    @abstractmethod
    def award_gift(self, gift):
        pass

class PercentageDiscount(DiscountStrategy):
    def calulate_discount(self, price: float) -> float:
        return price * 0.15

class FixedDiscount(DiscountStrategy):
    def calulate_discount(self, price: float) -> float:
        return 20

class ChristmasDiscount(DiscountStrategy):
    def calulate_discount(self, price: float) -> float:
        return price * 0.24

class DiscountCalculatorv2:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, price: float) -> float:
        return self.strategy.calulate_discount(price)