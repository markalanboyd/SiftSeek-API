import logging
from logging.handlers import RotatingFileHandler
import os


def configure_logging():
    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler(
        "logs/siftseek.log", maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    app_logger = logging.getLogger()
    app_logger.addHandler(file_handler)
    app_logger.setLevel(logging.INFO)
