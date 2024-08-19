import json
from typing import List, Dict, Any


import logging

def create_logger(log_file_path):
    """
    Функция для создания логгера, который будет записывать сообщения в файл.

    :param log_file_path: Путь к файлу, в который будет записываться лог.
    :return: Объект логгера.
    """
    # Создаем объект логгера
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Создаем файловый обработчик
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Форматируем сообщение
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем файловый обработчик к логгеру
    logger.addHandler(file_handler)

    return logger

# Пример использования
logger = create_logger('logs/my_app.log')
logger.info('Пример сообщения, которое будет записано в файл лога.')
