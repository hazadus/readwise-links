"""Модуль для настройки логирования."""

import logging
import sys


def setup_logging():
    """Настраивает логирование для приложения."""
    # Настраиваем корневой логгер
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Создаем обработчик для вывода в консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Создаем форматтер для логов
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Добавляем обработчик к корневому логгеру
    root_logger.addHandler(console_handler)
