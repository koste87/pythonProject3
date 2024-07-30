import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("input_info", [
    "invalid_input",
    "Счет 123",  # слишком короткий номер счета
])
def test_mask_account_card_invalid_input(input_info):
    with pytest.raises(ValueError):
        mask_account_card(input_info)

