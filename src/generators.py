# generators.py

from typing import List, Dict, Iterator, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction['description']


# src/generators.py

def card_number_generator(start, stop):
    """Генератор, возвращающий номера карт в формате без пробелов"""
    for i in range(start, stop + 1):
        yield f"{i:016}"
