from os import path, remove
from .hh_parser import *
# DATA_PATH = r'%s' % os.path.abspath(os.path.join(os.getcwd(), 'data')).replace('\\', '/')

# Удаляем существующий файл лога, если он есть, чтобы создавать новый файл во время каждого выполнения
if path.isfile("log_text_loader.log"):
    remove("log_text_loader.log")

# Создаем Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создаем обработчик для записи данных в файл
logger_handler = logging.FileHandler('log_text_loader.log')
logger_handler.setLevel(logging.INFO)

# Создаем Formatter для форматирования сообщений в логе
logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# Добавляем Formatter в обработчик
logger_handler.setFormatter(logger_formatter)

# Добавляем обработчик в Logger
logger.addHandler(logger_handler)
logger.info('Logging successfully started!')
