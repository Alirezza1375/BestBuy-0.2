import products
import store
import sys

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.Product("Sonny", 1500, 50)
               ]


def start(product_lst):
    """
        Displays a store menu and handles user commands to list products, show total quantity and make an order
    """

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

            print("When you want to finish order, enter empty string")
            shopping_list = []

            while True:
                s = store.Store(product_lst)
                active_products = s.get_all_products()
                for idx, p in enumerate(active_products):
                    print(f"{idx + 1}. {p.show()}")
                product_num = input("Which product # do you want? ")
                purchase_quantity = input("What amount do you want? ")

                if product_num == "" and purchase_quantity == "":
                    if not shopping_list:
                        print("No products selected. Returning to menu.")
                        break
                    try:
                        total_price = s.order(shopping_list)
                        print(f"Order complete! Total price: ${total_price:.2f}")

                    except Exception as e:
                        print(f"Error processing the order: {e}")
                    break

                try:
                    product_num = int(product_num)
                    purchase_quantity = int(purchase_quantity)
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue

                if 1 <= product_num <= len(active_products):
                    selected_product = active_products[product_num - 1]
                    available_quantity = selected_product.get_quantity()

                    if purchase_quantity > available_quantity:
                        print(
                            f"Not enough stock for {selected_product.name}. "
                            f"Only {available_quantity} available."
                        )
                        continue

                    final_purchase = (selected_product, purchase_quantity)
                    shopping_list.append(final_purchase)
                    print("Product added to list!")

                    active_products = s.get_all_products()
                else:
                    print("Invalid product number. Please try again.")

        if cmd == "4":
            print("ByeBye")
            sys.exit()


start(product_list)
