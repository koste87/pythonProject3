import os
import requests
from typing import Dict, Any


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли. Если валюта не RUB, использует внешний API для получения курса.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    currency = transaction.get('currency')
    amount = transaction.get('amount')

    if currency == 'RUB':
        return float(amount)

    api_key = os.getenv('API_KEY')
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
        headers={"apikey": api_key}
    )

    data = response.json()
    return float(data['result'])
