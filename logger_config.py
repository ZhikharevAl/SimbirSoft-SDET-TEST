import logging
import sys

"""
Эта функция настраивает логгер для записи сообщений в файл и вывода в консоль.
:param name: Имя логгера.
:param filepath: Путь к файлу, в который будут записываться сообщения.
:param file_level: Уровень логирования для файла.
:param console_level: Уровень логирования для консоли.
:return: Настроенный логгер.
"""


def configure_logger(name, filepath, file_level=logging.DEBUG,
                     console_level=logging.INFO):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(filepath)
        file_handler.setLevel(file_level)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
