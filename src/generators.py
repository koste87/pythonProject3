# generators.py

from typing import List, Dict, Iterator, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует банковские операции по заданной валюте.

    :param transactions: Список словарей с банковскими операциями
    :param currency_code: Строка, обозначающая валюту (например, 'USD')
    :return: Итератор с операциями в заданной валюте
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Возвращает описания всех банковских операций.

    :param transactions: Список словарей с банковскими операциями
    :return: Итератор с описаниями операций
    """
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, возвращающий номера карт в формате "XXXX XXXX XXXX XXXX".

    :param start: Начальное значение для генерации номеров
    :param stop: Конечное значение для генерации номеров
    :return: Итератор строк с номерами карт в формате "XXXX XXXX XXXX XXXX"
    """
    for i in range(start, stop + 1):
        card_number = f"{i:016}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
