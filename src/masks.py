# src/masks.py
import logging


# Функция для настройки логирования
def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Настраивает и возвращает логгер с заданным именем и уровнем логирования.

    Args:
        name (str): Имя логгера, обычно __name__.
        log_file (str): Путь к файлу для записи логов.
        level (int): Уровень логирования (по умолчанию DEBUG).

    Returns:
        logging.Logger: Настроенный объект логгера.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Создание обработчика записи в файл
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(level)

    # Формат логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика в логгер
    if not logger.handlers:  # Чтобы избежать добавления обработчиков при каждом вызове
        logger.addHandler(file_handler)

    return logger


# Настройка логгера для masks
logger = setup_logger(__name__, 'logs/masks.log')


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (int): Номер банковской карты.

    Returns:
        str: Замаскированный номер карты в формате 'XXXX XX** **** XXXX'.
    """
    logger.debug(f"Маскировка номера карты: {card_number}")
    card_str = str(card_number)
    if len(card_str) <= 10:
        logger.error("Номер карты слишком короткий для маскирования.")
        raise ValueError("Номер карты слишком короткий для маскирования.")

    masked_number = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info(f"Успешная маскировка номера карты: {masked_number}")
    return masked_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (int): Номер банковского счета.

    Returns:
        str: Замаскированный номер счета в формате '**XXXX'.
    """
    logger.debug(f"Маскировка номера счета: {account_number}")
    if not isinstance(account_number, int):
        logger.error("Номер счета должен быть числом.")
        raise TypeError("Номер счета должен быть числом.")

    masked_account = f"**{str(account_number)[-4:]}"
    logger.info(f"Успешная маскировка номера счета: {masked_account}")
    return masked_account

