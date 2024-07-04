import os
import time
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


def prepare_time():
    log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    console_time = datetime.now()
    return log_time, console_time


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
                        f'{datetime.now(timezone.utc).strftime("%Y-%m-%d_%H:%M:%S.%f")[:-3]}_{self.__app_name}.log'
        log_file_path = os.path.join(self.__log_catalog_path, log_file_name)
        self.__file = open(log_file_path, 'w+')
        self.__script_start_time = time.time()

    """
    Simple log message eg. "LOG: [2005-03-19 15:10:26.618]      simple_example"
    @:param text: Text to be logged
    """

    def log(self, text: str):
        log_time, console_time = prepare_time()
        print(f"LOG: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + f"LOG: [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Debug message eg. "DEBUG: [2005-03-19 15:10:26.618]      debug_example"
    @:param text: Text to be logged
    """
    def debug(self, text: str):
        log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        console_time = datetime.now()
        print(f"DEBUG: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.MAGENTA + f"DEBUG: [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Info message eg. "INFO: [2005-03-19 15:10:26.618]      info_example"
    @:param text: Text to be logged
    """
    def info(self, text: str):
        log_time, console_time = prepare_time()
        print(f"INFO: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + f"INFO: [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Warning message eg. "WARNING: [2005-03-19 15:10:26.618]      warning_example"
    @:param text: Text to be logged
    """
    def warning(self, text: str):
        log_time, console_time = prepare_time()
        print(f"WARNING: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + Back.YELLOW + "WARNING: " + Style.RESET_ALL
                  + Fore.YELLOW + f" [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Success message eg. "SUCCESS: [2005-03-19 15:10:26.618]      success_example"
    @:param text: Text to be logged
    """
    def success(self, text: str):
        log_time, console_time = prepare_time()
        print(f"SUCCESS: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.GREEN + f"SUCCESS: [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Error message eg. "ERROR: [2005-03-19 15:10:26.618]      error_example"
    @:param text: Text to be logged
    """
    def error(self, text: str):
        log_time, console_time = prepare_time()
        print(f"ERROR: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.RED + f"ERROR: [{console_time}]: \t {text}" + Style.RESET_ALL)
    """
    Critical message eg. "CRITICAL: [2005-03-19 15:10:26.618]      critical_example"
    @:param text: Text to be logged
    """
    def critical(self, text: str):
        log_time, console_time = prepare_time()
        print(f"CRITICAL: [{log_time}]: \t {text}", file=self.__file)
        if self.__log_to_console:
            print(Fore.WHITE + Back.RED + "CRITICAL:"
                  + Style.RESET_ALL + Fore.RED + f" [{console_time}]: \t {text}" + Style.RESET_ALL)

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
