import os
import time
import multiprocessing
from datetime import datetime, timezone

from colorama import Fore, Style, Back

from .SingletonMeta import SingletonMeta

"""
Logger class used to log messages to file and console
:param app_name: Name of the app
:param id: ID of the instance
:param log_catalog_path: Path to the log catalog
:param log_to_console: Flag to log messages to console

Example usage:
    logger = Logger("example", "1", "logs", True) 
    logger.log("This is a log message") # WHITE TEXT
    logger.debug("This is a debug message") # MAGENTA TEXT
    logger.info("This is an info message") # WHITE TEXT
    logger.warning("This is a warning message") # WHITE TEXT WITH YELLOW BACKGROUND
    logger.success("This is a success message") # GREEN TEXT
    logger.error("This is an error message") # RED TEXT
    logger.critical("This is a critical message") # RED TEXT WITH RED BACKGROUND
"""


file_lock = multiprocessing.Lock()

def prepare_time():
    log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    console_time = datetime.now()
    return log_time, console_time


def create_message(text: str, additional_prefix: str, log_type: str) -> str:
    log_time, console_time = prepare_time()
    return f"{log_type}{' ' + additional_prefix if additional_prefix else ''}: [{log_time}]: \t {text}"



class Logger(metaclass=SingletonMeta):
    __file = None

    def __init__(self, app_name=None, id=None, log_catalog_path=None, log_to_console=False):
        self.__log_catalog_path = log_catalog_path
        self.__app_name = app_name
        self.__instance_id = id
        self.__log_to_console = log_to_console
        self.test_init()

        os.makedirs(self.__log_catalog_path, exist_ok=True)

        # Create the log file path with a safe filename
        log_file_name = f'{self.__app_name}_{self.__instance_id}_logs_' \
                        f'{datetime.now(timezone.utc).strftime("%Y-%m-%d_%H:%M:%S.%f")[:-3]}.log'
        log_file_path = os.path.join(self.__log_catalog_path, log_file_name)
        self.__file = open(log_file_path, 'w+')
        self.__script_start_time = time.time()

    """
    Simple log message eg. "LOG: [2005-03-19 15:10:26.618]      simple_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix LOG)
    """

    def log(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'LOG')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + message + Style.RESET_ALL)

    """
    Debug message eg. "DEBUG: [2005-03-19 15:10:26.618]      debug_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix DEBUG)
    """

    def debug(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'DEBUG')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.MAGENTA + message + Style.RESET_ALL)

    """
    Info message eg. "INFO: [2005-03-19 15:10:26.618]      info_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix INFO)
    """

    def info(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'INFO')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + message + Style.RESET_ALL)

    """
    Warning message eg. "WARNING: [2005-03-19 15:10:26.618]      warning_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix WARNING)
    """

    def warning(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'WARNING')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.YELLOW + message + Style.RESET_ALL)

    """
    Success message eg. "SUCCESS: [2005-03-19 15:10:26.618]      success_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix SUCCESS)
    """

    def success(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'SUCCESS')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.GREEN + message + Style.RESET_ALL)

    """
    Error message eg. "ERROR: [2005-03-19 15:10:26.618]      error_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix ERROR)
    """

    def error(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'ERROR')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.RED + message + Style.RESET_ALL)

    """
    Critical message eg. "CRITICAL: [2005-03-19 15:10:26.618]      critical_example"
    @:param text: Text to be logged
    @:param additional_prefix: Text to be inserted before LOG TYPE NAME eg. (prefix CRITICAL)
    """

    def critical(self, text: str, additional_prefix: str = None):
        message = create_message(text, additional_prefix, 'CRITICAL')
        with file_lock:
            print(message, file=self.__file)
        if self.__log_to_console:
            print(Fore.BLACK + Back.RED + message + Style.RESET_ALL)

    def test_init(self):
        if not self.__log_catalog_path:
            raise TypeError("Log catalog path not set")
        if not self.__app_name:
            raise TypeError("Instance name not set")
        if not self.__instance_id:
            raise TypeError("Instance number not set")

    def __del__(self):
        if self.__file:
            self.__file.close()
            self.__file = None
