# Обработчик Финансовых Транзакций

Этот проект обрабатывает финансовые транзакции, читая данные из различных форматов, маскирует конфиденциальную информацию и ведет журнал действий и ошибок. Проект включает функциональность для чтения данных из JSON, CSV и Excel файлов, маскировки номеров карт и счетов, а также ведение логов.

## Структура Проекта

.
├── data
│ ├── 123.py
│ ├── init.py
│ ├── operations.json
│ ├── transactions.csv
│ └── transactions_excel.xlsx
├── decorators
│ └── init.py
├── src
│ ├── init.py
│ ├── decorators.py
│ ├── external_api.py
│ ├── filter_by_word.py
│ ├── generators.py
│ ├── main.py
│ ├── masks.py
│ ├── processing.py
│ ├── utils.py
│ └── widget.py
└── logs
├── masks.log
└── utils.log


## Особенности

- **Чтение Транзакций**:
  - Загрузка транзакций из файлов JSON, CSV и Excel.
  
- **Маскирование Данных**:
  - Маскировка номеров кредитных карт.
  - Маскировка номеров счетов.

- **Логирование**:
  - Логи для модулей `utils` и `masks` сохраняются в директории `logs`.
  - Включает метки времени, имена модулей, уровни серьезности и сообщения.

## Настройка

### Требования

- Python 3.x
- Необходимые библиотеки: `pandas`, `json`, `csv`, `logging`

Установите необходимые библиотеки с помощью:

```bash
pip install pandas
Структура Директории
Структура директорий должна быть следующей:

.
├── data
│   ├── 123.py
│   ├── __init__.py
│   ├── operations.json
│   ├── transactions.csv
│   └── transactions_excel.xlsx
├── decorators
│   └── __init__.py
├── src
│   ├── __init__.py
│   ├── decorators.py
│   ├── external_api.py
│   ├── filter_by_word.py
│   ├── generators.py
│   ├── main.py
│   ├── masks.py
│   ├── processing.py
│   ├── utils.py
│   └── widget.py
└── logs
    ├── masks.log
    └── utils.log
Модули
src/utils.py
Содержит функции для чтения транзакций:

get_transactions_dictionary(path: str) -> dict: Читает JSON-файл и возвращает данные о транзакциях в виде словаря.
get_transactions_dictionary_csv(csv_path: str) -> list[dict]: Читает CSV-файл и возвращает данные о транзакциях в виде списка словарей.
get_transactions_dictionary_excel(excel_path: str) -> list[dict]: Читает Excel-файл и возвращает данные о транзакциях в виде списка словарей.
src/masks.py
Содержит функции для маскировки конфиденциальной информации:

get_mask_card_number(card_number: str) -> str: Маскирует номер кредитной карты.
get_mask_account(macc_number: str) -> str: Маскирует номер счета.
Логирование
Логирование настроено для модулей utils и masks. Логи сохраняются в директории logs. Настройки логирования включают:

Отдельные логгеры для utils и masks.
Логи сохраняются в директории logs с расширением .log.
Формат записи логов включает метку времени, имя модуля, уровень серьезности и сообщение.
Логи перезаписываются при каждом запуске.
Пример Настройки Логирования
import logging

# Настройка логирования для модуля utils
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="logs/utils.log",
    filemode="w",
)
utils_logger = logging.getLogger("app.utils")

# Настройка логирования для модуля masks
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="logs/masks.log",
    filemode="w",
)
masks_logger = logging.getLogger("app.masks")
Использование
Для использования функций и логгеров:

from src.utils import get_transactions_dictionary, get_transactions_dictionary_csv, get_transactions_dictionary_excel
from src.masks import get_mask_card_number, get_mask_account

# Пример использования
transactions_json = get_transactions_dictionary("data/operations.json")
transactions_csv = get_transactions_dictionary_csv("data/transactions.csv")
transactions_excel = get_transactions_dictionary_excel("data/transactions_excel.xlsx")

masked_card = get_mask_card_number("1234567812345678")
masked_account = get_mask_account("1234567890123456")
Тестирование
Юнит-тесты предоставлены для проверки функциональности. Запустите тесты с помощью:

pytest
