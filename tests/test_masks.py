import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize("input_card_number, expected_masked_number", [
    (1234567890123456, "1234 56** **** 3456"),
    (9876543210987654, "9876 54** **** 7654"),
    (1234, "1234 **"),
    (9876543210, "9876 **"),
])
def test_get_mask_card_number(input_card_number, expected_masked_number):
    assert get_mask_card_number(input_card_number) == expected_masked_number


def test_get_mask_card_number_invalid_input():
    with pytest.raises(TypeError):
        get_mask_card_number("invalid_input")


# Add more tests for edge cases and invalid inputs as needed


import pytest
from src.masks import get_mask_account


@pytest.mark.parametrize("input_account_number, expected_masked_account", [
    (1234567890123456, "**3456"),
    (9876543210987654, "**7654"),
    (1234, "**1234"),
    (9876543210, "**3210"),
])
def test_get_mask_account(input_account_number, expected_masked_account):
    assert get_mask_account(input_account_number) == expected_masked_account


def test_get_mask_account_invalid_input():
    with pytest.raises(TypeError):
        get_mask_account("invalid_input")

# Add more tests for edge cases and invalid inputs as needed
