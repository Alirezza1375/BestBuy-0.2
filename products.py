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


