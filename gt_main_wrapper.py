import sys
from main import Main


def call_main():
    """
    ***********************************************
    * This is the driver code. Don't change it!!!
    * *********************************************

    Format of the 'args' array: [`<COMMAND_NAME_1> <ARG1> <ARG2> .. <ARG N>`, `<COMMAND_NAME_2> <ARG1> <ARG2> .. <ARG N>`]
    Example: ["PLACE_ORDER 101 Apple 5", "TOTAL_COST 101"]

    The code evaluator will execute this code by using the command:
    python main.py "PLACE_ORDER 101 Apple 5" "TOTAL_COST 101"

    We loop through the list of commands passed in as input arguments and handle each one of them.
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    commands = sys.argv[1:]
    main = Main()

    for command in commands:
        main.handle(command)


if __name__ == "__main__":
    call_main()
