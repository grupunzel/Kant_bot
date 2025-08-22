import logging
from logging import getLogger, StreamHandler, basicConfig
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = getLogger(__name__)
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    file_handler = RotatingFileHandler(
        "logs/main.log",
        maxBytes=1024 * 1024,
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel('INFO')

    stream_handler = StreamHandler()
    stream_handler.setLevel('ERROR')

    basicConfig(
        level=logging.DEBUG,
        format=FORMAT,
        handlers=[file_handler, stream_handler]
    )
    return logger

logger = setup_logger()