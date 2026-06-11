from shopping_cart import ShoppingCart

class Main:
    """
    ***********************************************
    * This is the driver code. Don't change it!!!
    ***********************************************
    """

    @staticmethod
    def main():
        orders = [
            "Regular Electronics:100:2 Books:20:1",
            "Member Clothing:50:4",
            "VIP Electronics:100:1 Clothing:50:2",
            "Gold Books:20:1",
            "Regular Toys:30:2"
        ]

        import sys

        if len(sys.argv) < 2:
            print("Arguments are required to run the program.")
            return

        Main.handle(sys.argv[1], orders)

    @staticmethod
    def handle(input_str, orders):
        for order in orders:
            if order == input_str:
                # Forward input to ShoppingCart
                shopping_cart_args = [order]
                ShoppingCart.main(shopping_cart_args)
                return


if __name__ == "__main__":
    Main.main()