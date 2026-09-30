import pytest
from shopping_summary import calculate_total, find_most_expensive, format_receipt

SHOPPING_LIST = [
    ("Apples", 1.5),
    ("Bananas", 0.75),
    ("Cookies", 2.5),
    ("Dairy Milk", 3.5),
    ("Rice", 1.5),
]


def test_calculate_total():
    assert calculate_total(SHOPPING_LIST) == pytest.approx(9.75)


def test_calculate_total_empty_list():
    assert calculate_total([]) == 0


def test_find_most_expensive():
    assert find_most_expensive(SHOPPING_LIST) == ("Dairy Milk", 3.5)


def test_format_receipt_contains_item_names():
    receipt = format_receipt(SHOPPING_LIST)
    assert "Apples" in receipt
    assert "Dairy Milk" in receipt