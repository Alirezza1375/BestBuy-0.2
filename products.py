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

        if self.name == "" or self.price < 0 or self.quantity < 0:
            raise ValueError("Something went wrong!")

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
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
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
        return f"{self.name}: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        :param quantity:
        """
        if self.quantity == 0 or quantity > self.quantity or not self.active:
            raise Exception("Something went wrong!!")
        else:
            self.quantity -= quantity
            return float(self.price * quantity)


