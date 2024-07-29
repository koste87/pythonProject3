# Функция маскировки номера банковской карты
def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (int): Номер банковской карты.

    Returns:
        str: Замаскированный номер карты в формате 'XXXX XX** **** XXXX'.
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


# Функция маскировки номера банковского счета
def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (int): Номер банковского счета.

    Returns:
        str: Замаскированный номер счета в формате '**XXXX'.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"


# Пример использования функций
print(get_mask_card_number(7000792289606361))  # Вывод: 7000 79** **** 6361
print(get_mask_account(73654108430135874305))  # Вывод: **4305
