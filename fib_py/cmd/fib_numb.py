import argparse

from fib_py.fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate the Fibonacci number of a given number."
    )
    parser.add_argument("--number", action='store', type=int, required=True,
                        help="The number to calculate the Fibonacci number of.")

    args = parser.parse_args()
    print(
        f"The Fibonacci number of {args.number} is: "
        f"{recurring_fibonacci_number(number=args.number)}."
    )
