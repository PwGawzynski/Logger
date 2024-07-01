import os
import time
from datetime import datetime, timezone

from .SingletonMeta import SingletonMeta

"""
Logger class used to log events
@:param name: Name used to identify instance
@:param id: ID used to identify instance
@:param log_catalog_path: Path to log catalog
@:param logs_catalog_name: Name of log catalog
"""


class Logger(metaclass=SingletonMeta):
    __file = None

    def __init__(self, name=None, id=None, log_catalog_path=None, logs_catalog_name=None):
        self.__log_catalog_path = log_catalog_path
        self.__instance_name = name
        self.__instance_number = id
        self.__log_catalog_name = logs_catalog_name
        self.test_init()

        os.makedirs(self.__log_catalog_path, exist_ok=True)

        # Create the log file path with a safe filename
        log_file_name = f'logs_{datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")}_{self.__instance_name}_{self.__instance_number}.txt'
        log_file_path = os.path.join(self.__log_catalog_path, log_file_name)
        self.__file = open(log_file_path, 'w+')
        self.__script_start_time = time.time()
        self.log('START SCRAPING')

    def __calculate_time(self):
        end_time = time.time() - self.__script_start_time
        print(f'EXECUTION TIME: {end_time}', file=self.__file)

    def log(self, text: str):
        log_time = datetime.now(timezone.utc)
        console_time = datetime.now()
        print(f"LOG: [{log_time}]: \t {text}", file=self.__file)
        print(f"LOG: [{console_time}]: \t {text}")

    def test_init(self):
        if not self.__log_catalog_path:
            raise TypeError("Log catalog path not set")
        if not self.__instance_name:
            raise TypeError("Instance name not set")
        if not self.__instance_number:
            raise TypeError("Instance number not set")
        if not self.__log_catalog_name:
            raise TypeError("Log catalog name not set")

    def __del__(self):
        if self.__file:
            self.log('END SCRAPING')
            self.__calculate_time()
            self.__file.close()
            self.__file = None
