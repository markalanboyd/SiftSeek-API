import logging
from logging.handlers import RotatingFileHandler
import os


def configure_logging() -> None:
    """
    Configures application-wide logging with a rotating file handler.

    This function sets up logging to write messages to a file, ensuring that log
    files are rotated when they reach a certain size. It checks if a 'logs' directory
    exists, and if not, creates it. Logs are written to 'logs/siftseek.log'. Each log
    file is limited to 10KB, and a maximum of 10 backup files are kept.

    The log format includes the timestamp, log level, message, and the file and line
    number from where the log was generated. The logging level is set to INFO for both
    the file handler and the application logger.

    No parameters are required and no value is returned. The function is intended to be
    called at application startup to configure logging for the entire application lifecycle.
    """
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
