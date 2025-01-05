class Product:
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception
        :param name:
        :param price:
        :param quantity:
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not self.name:
            raise ValueError("Product name can not be empty!")
        if self.price < 0:
            raise ValueError("Price can not be negative!")
        if self.quantity < 0:
            raise ValueError("Quantity can not be negative!")

    def get_quantity(self):
        """
        Getter function for quantity.
        Returns the quantity (float).

        """
        return int(self.quantity)

    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        :param quantity:
        """

        if quantity < 0:
            raise ValueError("quantity can not be negative!")
        self.quantity = quantity

    def is_active(self):
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        self.active = self.quantity > 0
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string that represents the product
        """
        return f"{self.name}: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        :param quantity:
        """
        if quantity > self.quantity:
            raise Exception("Requested quantity exceeds available stock.")
        self.quantity -= quantity
        self.active = self.quantity > 0
        return float(self.price * quantity)


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """
        A product that does not need quantity tracking.
        """
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        """
            Overriding the set_quantity method to prevent changes to the quantity.
        """
        raise ValueError("Quantity for non-stock product can not be modified.")

    def show(self):
        """
            Overriding the show method to indicate that this is a non-stock product.
        """
        return f"{self.name} (Non-stocked product): ${self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity,  max_purchase):
        """
            A product that can be only purchased a limited number of times in an order.
        """
        super().__init__(name, price, quantity)
        self.max_purchase = max_purchase

    def buy(self, quantity):
        """
            Overriding the buy method to enforce a limit on how many can be bought in one order.
        """
        if quantity > self.max_purchase:
            raise ValueError(f"Cannot purchase more than {self.max_purchase} of {self.name}")
        return super().buy(quantity)

    def show(self):
        """
            Overriding the show method to indicate that this is a limited product.
        """
        return f"{self.name} (Limited product, max purchase: {self.max_purchase}): ${self.price}"
