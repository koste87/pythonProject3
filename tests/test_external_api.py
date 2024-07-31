import json
from typing import List, Dict, Any


def read_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    :param filepath: Путь до файла JSON.
    :return: Список словарей с данными о транзакциях. Если файл не найден или формат неправильный, возвращает пустой список.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
