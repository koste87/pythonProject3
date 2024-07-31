
### Описание модулей

- `src/masks.py`: Содержит функции для маскирования номеров карт и счетов.
- `src/processing.py`: Содержит функции для фильтрации и сортировки данных.
- `src/widget.py`: Содержит функции для обработки различных типов данных.

### Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd your_project
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### Тестирование

Проект использует библиотеку `pytest` для тестирования.

#### Запуск тестов

Для запуска всех тестов используйте команду:

```bash
pytest


# Проект

## Описание

Этот проект предназначен для демонстрации и тестирования различных функций, связанных с маскированием номеров карт и счетов, а также фильтрацией и сортировкой данных, используя генераторы Python.

## Структура проекта

your_project/
├── src/
│ ├── init.py
│ ├── generators.py
│ ├── masks.py
│ ├── processing.py
│ └── widget.py
├── tests/
│ ├── init.py
│ ├── test_generators.py
│ ├── test_masks.py
│ ├── test_processing.py
│ └── test_widget.py
└── README.md


## Новый модуль `generators`

В новом модуле `generators` реализованы функции для работы с данными транзакций через генераторы:

### Функции

- `filter_by_currency(transactions, currency)`: Возвращает итератор, фильтрующий транзакции по заданной валюте.
- `transaction_descriptions(transactions)`: Генератор, возвращающий описание каждой операции по очереди.
- `card_number_generator(start, stop)`: Генератор, выдающий номера банковских карт в заданном диапазоне.

### Примеры использования

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
    {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
    {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"}
]

# Фильтрация транзакций по валюте USD
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)

# Вывод описаний транзакций
descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)

# Генерация номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)