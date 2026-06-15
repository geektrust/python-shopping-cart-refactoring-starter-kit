class ShoppingCart:

    DISCOUNTS = {
        "Regular": 0,
        "Member": 10,
        "VIP": 20
    }

    SHIPPING_COSTS = {
        "Electronics": 10,
        "Books": 0,
        "Clothing": 5
    }

    @staticmethod
    def main(args):
        """
        Format of args:
        ["Regular Electronics:100:2 Books:20:1"]
        """
        ShoppingCart.handle(args[0])

    @staticmethod
    def handle(input):
        parts = input.split()

        customer = parts[0]

        if customer not in ShoppingCart.DISCOUNTS:
            print("INVALID CUSTOMER TYPE")
            return

        discount = ShoppingCart.DISCOUNTS[customer]

        subtotal = 0
        shipping = 0

        for item_str in parts[1:]:
            item = item_str.split(":")

            category = item[0]
            price = int(item[1])
            quantity = int(item[2])

            if category not in ShoppingCart.SHIPPING_COSTS:
                print("INVALID CATEGORY")
                return

            subtotal += price * quantity
            shipping += ShoppingCart.SHIPPING_COSTS[category] * quantity

        total = subtotal - (subtotal * discount / 100)

        if customer != "VIP":
            total += shipping

        print(f"Order Total: {total:.2f}")
