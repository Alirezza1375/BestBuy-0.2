import products
import store
import sys

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.Product("Sonny", 1500, 50)
               ]


def start(product_lst):

    while True:
        print("Store menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        cmd = input("choose a command from 1 to 4: ")
        if cmd == "1":
            s = store.Store(product_lst)
            for idx, p in enumerate(s.get_all_products()):
                print(f"{idx+1}. {p.show()}")
        if cmd == "2":
            q = store.Store(product_lst)
            print(f"total of {q.get_total_quantity()} items in the store.")

        if cmd == "3":
            s = store.Store(product_lst)
            print("Available products:")
            for idx, p in enumerate(s.get_all_products()):
                print(f"{idx + 1}. {p.show()}")

            shopping_list = []

            print("When you want to finish the order, press Enter at the 'Which product # prompt.")

            while True:

                product_num = input("Which product # do you want? ")

                if product_num == "":
                    if shopping_list:
                        try:
                            total_price = s.order(shopping_list)
                            print(f"Order completed! Total price: ${total_price:.2f}")
                        except Exception as e:
                            print(f"Error processing the order: {e}")
                    else:
                        print("No items were added to the order.")
                    break

                # Validate product number
                try:
                    product_num = int(product_num)

                    if 1 <= product_num <= len(product_lst):
                        selected_product = product_lst[product_num - 1]

                        # Ask for quantity
                        quantity = input(f"What amount do you want for {selected_product.name}? ")
                        try:
                            quantity = int(quantity)

                            if quantity > 0:
                                shopping_list.append((selected_product, quantity))
                                print("Product added to list!")
                            else:
                                print("Quantity must be a positive integer.")
                        except ValueError:
                            print("Invalid quantity input. Please enter a valid number.")
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid product number. Please enter a valid number.")
        if cmd == "4":
            print("ByeBye")
            sys.exit()


start(product_list)

