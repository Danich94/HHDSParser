import logging
from logging.config import dictConfig

LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "simple_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%y %H:%M:%S"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "simple_formatter",
            "filename": "log_text_loader.log"
        },
    },
    "loggers": {
        "root": {
            "handlers": ["file_handler"],
            "level": "INFO",
        }
    },
}


# Logging functions
def text_loader_logging():
    logging.config.dictConfig(LOG_CONFIG)
    logger_obj = logging.getLogger(__name__)
    return logger_obj
