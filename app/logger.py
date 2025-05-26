import logging
from logging.handlers import RotatingFileHandler
import sys

# Создаем логгер
logger = logging.getLogger("task_tracker")
# Можно менять уровень (DEBUG, INFO, WARNING, ERROR)
logger.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Логирование в файл с ротацией (максимум 5 файлов по 5 МБ)
file_handler = RotatingFileHandler(
    "logs/task_tracker.log", maxBytes=5*1024*1024, backupCount=5)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# Логирование в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)
