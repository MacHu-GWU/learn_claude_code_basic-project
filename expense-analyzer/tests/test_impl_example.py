"""
Test file for the example implementation (reference answer).

This file tests the impl_example.py to ensure the reference answer is correct.

Students should complete impl.py and then tests/test_impl.py should pass.
"""

from expense_analyzer.impl_example import main


def test_main_returns_dict():
    """Test that main() returns the final result dictionary."""
    result = main()
    assert isinstance(result, dict)
    assert len(result) == 6


def test_main_has_all_categories():
    """Test that main() result contains all 6 categories."""
    result = main()
    expected_categories = {"Dining", "Transport", "Shopping", "Entertainment", "Groceries", "Utilities"}
    assert set(result.keys()) == expected_categories


def test_main_correct_max_expenses():
    """
    Test that main() finds the correct maximum expenses for Q3 2025.

    Expected results:

    - Dining: TXN-2025-089 ($320.00)
    - Transport: TXN-2025-074 ($58.20)
    - Shopping: TXN-2025-076 ($449.00)
    - Entertainment: TXN-2025-077 ($199.00)
    - Groceries: TXN-2025-069 ($198.50)
    - Utilities: TXN-2025-073 ($145.80)
    """
    result = main()

    expected_results = {
        "Dining": "TXN-2025-089",
        "Transport": "TXN-2025-074",
        "Shopping": "TXN-2025-076",
        "Entertainment": "TXN-2025-077",
        "Groceries": "TXN-2025-069",
        "Utilities": "TXN-2025-073",
    }

    for category, expected_id in expected_results.items():
        assert result[category] == expected_id, \
            f"{category}: expected {expected_id}, got {result.get(category)}"
