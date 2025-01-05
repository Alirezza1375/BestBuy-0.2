import products
import store
import promotions
import sys

# Create product list with promotions
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, max_purchase=1)
]

# Create promotions
percentage_discount = promotions.PercentageDiscount("20% off", 20)
second_item_half_price = promotions.SecondItemHalfPrice("Second Item at Half Price")
buy2_get1_free = promotions.Buy2Get1Free("Buy 2, Get 1 Free")

# Assign promotions to products
product_list[0].set_promotion(percentage_discount)  # MacBook Air M2
product_list[1].set_promotion(second_item_half_price)  # Bose QuietComfort Earbuds
product_list[2].set_promotion(buy2_get1_free)  # Google Pixel 7


def start(product_lst):
    """
    Displays a store menu and handles user commands to list products,
    show total quantity, make an order, and apply promotions.
    """
    store_instance = store.Store(product_lst)

    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        cmd = input("Choose a command from 1 to 4: ")

        if cmd == "1":
            # List all active products
            print("\nProducts available in the store:")
            for idx, p in enumerate(store_instance.get_all_products()):
                print(f"{idx + 1}. {p.show()}")

        elif cmd == "2":
            # Show total amount in store
            total_quantity = store_instance.get_total_quantity()
            print(f"\nTotal quantity of items in store: {total_quantity}")

        elif cmd == "3":
            # Make an order
            print("\nWhen you want to finish order, enter an empty string.")
            shopping_list = []

            while True:
                active_products = store_instance.get_all_products()
                for idx, p in enumerate(active_products):
                    print(f"{idx + 1}. {p.show()}")

                product_num = input("Which product # do you want? ")
                purchase_quantity = input("What amount do you want? ")

                # Finish the order
                if product_num == "" and purchase_quantity == "":
                    if not shopping_list:
                        print("\nNo products selected. Returning to menu.")
                        break

                    try:
                        # Process the order
                        total_price = store_instance.order(shopping_list)
                        print(f"\nOrder complete! Total price: ${total_price:.2f}")
                    except Exception as e:
                        print(f"Error processing the order: {e}")
                    break

                try:
                    # Convert inputs to integers
                    product_num = int(product_num)
                    purchase_quantity = int(purchase_quantity)

                    # Validate product number
                    if 1 <= product_num <= len(active_products):
                        selected_product = active_products[product_num - 1]

                        # Validate stock and apply promotions
                        available_quantity = selected_product.get_quantity()
                        if isinstance(selected_product, products.LimitedProduct):
                            if purchase_quantity > selected_product.max_purchase:
                                print(f"\n{selected_product.name} can only be purchased "
                                      f"{selected_product.max_purchase} time(s) per order.")
                                continue

                        if isinstance(selected_product, products.NonStockedProduct):
                            print(f"\n{selected_product.name} does not track quantity. Adding to your order.")

                        elif purchase_quantity > available_quantity:
                            print(f"\nNot enough stock for {selected_product.name}. "
                                  f"Only {available_quantity} available.")
                            continue

                        # Add to shopping list
                        shopping_list.append((selected_product, purchase_quantity))
                        print(f"\n{selected_product.name} added to your shopping list!")

                    else:
                        print("\nInvalid product number. Please try again.")
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers.")

        elif cmd == "4":
            # Exit the program
            print("\nThank you for visiting! Goodbye!")
            sys.exit()

        else:
            print("\nInvalid command. Please select a valid option.")


start(product_list)
