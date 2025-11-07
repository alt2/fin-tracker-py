import argparse

from .loader import load_transactions


def main() -> None:
    """Command-line interface for the personal finance tracker."""
    parser = argparse.ArgumentParser(description="Personal finance tracker CLI")
    parser.add_argument(
        "--csv",
        type=str,
        default="data/sample.csv",
        help="Path to CSV file containing transactions",
    )
    args = parser.parse_args()

    transactions = load_transactions(args.csv)
    for t in transactions:
        print(f"{t.date}: {t.description} - {t.amount} ({t.category})")


if __name__ == "__main__":
    main()
