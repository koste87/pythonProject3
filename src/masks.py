# src/masks.py

def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (int): Номер банковской карты.

    Returns:
        str: Замаскированный номер карты в формате 'XXXX XX** **** XXXX'.
    """
    card_str = str(card_number)
    if len(card_str) <= 10:  # Изменяем на <= для более явной проверки
        raise ValueError("Номер карты слишком короткий для маскирования.")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


# Функция маскировки номера банковского счета
# src/masks.py

def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (int): Номер банковского счета.

    Returns:
        str: Замаскированный номер счета в формате '**XXXX'.
    """
    if not isinstance(account_number, int):
        raise TypeError("Номер счета должен быть числом.")
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
