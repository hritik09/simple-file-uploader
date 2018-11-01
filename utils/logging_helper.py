import logging
from logging import config

from settings import LOGGING_CONFIG

config.dictConfig(LOGGING_CONFIG)


def get_logger(module_name):
    logger = logging.getLogger(module_name)
    return logger
