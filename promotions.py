from abc import ABC, abstractmethod


class Promotion(ABC):

    """
        Abstract base clas for all promotions.
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
            Applies the promotion to the given product and quantity.
        """
        pass


class PercentageDiscount(Promotion):
    """
        A promotion that applies a percentage discount to the total price of a product.
    """
    def __init__(self, name, discount_percentage):
        super().__init__(name)
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        """
            Applies the percentage discount to the total price of a product.
        """
        total_price = product.price * quantity
        discount = total_price * (self.discount_percentage / 100)
        return total_price - discount


class SecondItemHalfPrice(Promotion):
    """
        A promotion where every second item is available at half price.
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
            Applies the promotion where every second item is available at half price.
        """
        total_price = 0
        for i in range(quantity):
            if i % 2 == 1:
                total_price += product.price / 2
            else:
                total_price += product.price
        return total_price


class Buy2Get1Free(Promotion):
    """
        A promotion where for every two items purchased, the third one is free.
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        total_price = 0
        groups_of_three = quantity // 3
        remaining_items = quantity % 3

        total_price += groups_of_three * 2 * product.price
        total_price += remaining_items * product.price

        return total_price

