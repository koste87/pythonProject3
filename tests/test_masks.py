import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("input_card_number, expected_masked_number", [
    (1234567890123456, "1234 56** **** 3456"),
    (9876543210987654, "9876 54** **** 7654"),
])
def test_get_mask_card_number(input_card_number, expected_masked_number):
    assert get_mask_card_number(input_card_number) == expected_masked_number

@pytest.mark.parametrize("input_card_number", [
    1234,  # слишком короткий номер карты
    987654321,  # слишком короткий номер карты (9 цифр)
    9876543210,  # слишком короткий номер карты (10 цифр)
])
def test_get_mask_card_number_invalid_input(input_card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(input_card_number)

@pytest.mark.parametrize("input_account_number, expected_masked_account", [
    (1234567890123456, "**3456"),
    (9876543210987654, "**7654"),
    (1234, "**1234"),
    (9876543210, "**3210"),
])
def test_get_mask_account(input_account_number, expected_masked_account):
    assert get_mask_account(input_account_number) == expected_masked_account

@pytest.mark.parametrize("input_account_number", [
    "invalid_input",  # строка вместо числа
    None,  # None вместо числа
])
def test_get_mask_account_invalid_input(input_account_number):
    with pytest.raises(TypeError):
        get_mask_account(input_account_number)
