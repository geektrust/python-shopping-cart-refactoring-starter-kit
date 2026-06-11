class ShoppingCart:

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

        if customer == "Regular":
            discount = 0
        elif customer == "Member":
            discount = 10
        elif customer == "VIP":
            discount = 20
        else:
            print("INVALID CUSTOMER TYPE")
            return

        subtotal = 0
        shipping = 0

        for item_str in parts[1:]:
            item = item_str.split(":")

            category = item[0]
            price = int(item[1])
            quantity = int(item[2])

            subtotal += price * quantity

            if category == "Electronics":
                shipping += 10 * quantity
            elif category == "Books":
                shipping += 0
            elif category == "Clothing":
                shipping += 5 * quantity
            else:
                print("INVALID CATEGORY")
                return

        total = subtotal - (subtotal * discount / 100)

        if customer != "VIP":
            total += shipping

        print(f"Order Total: {total:.2f}")