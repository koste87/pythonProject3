# src/widget.py

from src.masks import get_mask_card_number, get_mask_account

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    if info.startswith("Счет"):
        try:
            account_number = int(info.split()[1])
            if len(str(account_number)) < 4:
                raise ValueError("Account number too short")
            return f"Счет {get_mask_account(account_number)}"
        except (ValueError, IndexError):
            raise ValueError("Invalid account information")
    else:
        try:
            card_type, card_number = info.rsplit(' ', 1)
            card_number = int(card_number)
            return f"{card_type} {get_mask_card_number(card_number)}"
        except (ValueError, IndexError):
            raise ValueError("Invalid card information")


# src/widget.py

from datetime import datetime


def get_date(date_str: str) -> str:
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


# Пример для карты
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361

# Пример для счета
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

# Пример для даты
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
