"""
Expense Analyzer - A data analysis project using Polars SQL.

This module provides functions to analyze expense data from a TSV file.

TODO: Implement the functions below to complete the expense analyzer.
"""

import polars as pl
from pathlib import Path

# Default data file path
DEFAULT_DATA_FILE = Path(__file__).absolute().parent.parent / "expense.tsv"

# Q3 date range
DEFAULT_START_DATE = "2025-07-01"
DEFAULT_END_DATE = "2025-09-30"


def load_expense_data(
    file_path: str,
) -> pl.DataFrame:
    """
    Load expense data from a TSV file and print the dataframe.

    TODO: Use pl.read_csv() with separator="\t" to read the TSV file.

    Args:
        file_path: Path to the TSV file

    Returns:
        Polars DataFrame containing the expense data
    """
    # TODO: Read the TSV file and return the DataFrame
    # Hint: Use pl.read_csv(file_path, separator="\t")
    print("=== Loaded Expense Data ===")
    # print(df)
    # print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")
    # print(f"Columns: {df.columns}")
    pass


def preview_first_rows(
    df: pl.DataFrame,
    n: int = 5,
) -> pl.DataFrame:
    """
    Use SQL to select the first N rows from the dataframe.

    TODO: Use pl.sql() with a SELECT * FROM df LIMIT {n} query.

    Args:
        df: Polars DataFrame
        n: Number of rows to preview (default 5)

    Returns:
        DataFrame with first N rows
    """
    # TODO: Write a SQL query to select the first n rows
    # Hint: Use pl.sql(f"SELECT * FROM df LIMIT {n}").collect()
    print(f"\n=== First {n} Rows (SELECT * FROM df LIMIT {n}) ===")
    # print(df_out)
    pass


def filter_q3_data(
    df: pl.DataFrame,
    START_DATE: str = DEFAULT_START_DATE,
    END_DATE: str = DEFAULT_END_DATE,
) -> pl.DataFrame:
    """
    Filter data to Q3 2025 (July 1 - September 30).

    TODO: Use pl.sql() with a WHERE clause to filter by date range.

    Args:
        df: Polars DataFrame with expense data
        START_DATE: Start date for Q3 (default "2025-07-01")
        END_DATE: End date for Q3 (default "2025-09-30")

    Returns:
        DataFrame with only Q3 data
    """
    # TODO: Write a SQL query to filter by date range
    # Hint: WHERE date >= '{START_DATE}' AND date <= '{END_DATE}'
    print(f"\n=== Q3 Data ({START_DATE} to {END_DATE}) ===")
    # print(df_out)
    # print(f"\nFiltered to {df_out.shape[0]} rows in Q3")
    pass


def find_max_expense_per_category(
    df: pl.DataFrame,
) -> dict:
    """
    Find the maximum expense per category.

    TODO: Use Polars SQL with a window function or GROUP BY to find
    the transaction with the highest amount in each category.

    Args:
        df: Polars DataFrame with Q3 expense data

    Returns:
        Dictionary mapping category to transaction_id
        Example: {"Dining": "TXN-2025-089", "Transport": "TXN-2025-074", ...}
    """
    # TODO: Write a SQL query to find max expense per category
    # Hint: You can use ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC)
    # or GROUP BY with MAX(amount)
    print("\n=== Max Expense Per Category ===")
    # print(df_out)

    # TODO: Convert the result DataFrame to a dictionary
    # The dictionary should map category -> transaction_id
    # output = {}
    # for row in df_out.to_dicts():
    #     output[row["category"]] = row["transaction_id"]
    #     print(f"  {row['category']}: {row['transaction_id']} (${row['amount']:.2f} at {row['merchant']})")
    # return output
    pass


def main(
    DATA_FILE: Path = DEFAULT_DATA_FILE,
    START_DATE: str = DEFAULT_START_DATE,
    END_DATE: str = DEFAULT_END_DATE,
):
    """
    Main function to demonstrate all expense analysis functions.
    """
    file_path = str(DATA_FILE)

    print("=" * 60)
    print("EXPENSE ANALYZER - Demo Run")
    print("=" * 60)

    # Step 1: Load and display the data
    df = load_expense_data(file_path)

    # Step 2: Preview first 5 rows using SQL
    preview_first_rows(df)

    # Step 3: Filter to Q3 data
    df_q3 = filter_q3_data(df, START_DATE, END_DATE)

    # Step 4: Find max expense per category
    print("\n" + "=" * 60)
    print("FINAL RESULT: Max Expense Per Category")
    print("=" * 60)
    df_result = find_max_expense_per_category(df_q3)

    print("\n=== Summary Dictionary ===")
    for category in sorted(df_result.keys()):
        print(f"  '{category}': '{df_result[category]}'")

    return df_result


if __name__ == "__main__":
    main()
