from shopping_cart import ShoppingCart

class Main:

    ORDERS = [
        "Regular Electronics:100:2 Books:20:1",
        "Member Clothing:50:4",
        "VIP Electronics:100:1 Clothing:50:2",
        "Gold Books:20:1",
        "Regular Toys:30:2"
    ]

    @staticmethod
    def main():
        import sys

        if len(sys.argv) < 2:
            print("Arguments are required to run the program.")
            return

        Main.handle(sys.argv[1])

    @staticmethod
    def handle(input_str):
        for order in Main.ORDERS:
            if order == input_str:
                ShoppingCart.main([order])
                return


if __name__ == "__main__":
    Main.main()
