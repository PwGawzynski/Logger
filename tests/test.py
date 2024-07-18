import multiprocessing
import os
from multiprocessing import freeze_support

from logger.logger import Logger
try:
    multiprocessing.set_start_method('fork')
except RuntimeError:
    pass


lock = multiprocessing.Lock()
Logger("TEST_LOGGER", "1", "logs", True)


def test():
    with lock:
        for x in range(3):
            Logger.info(f"Test {x}")


processes = []
for i in range(3):
    process = multiprocessing.Process(target=test)
    process.start()
    processes.append(process)
for process in processes:
    process.join()

current_dir = os.path.dirname(os.path.abspath(__file__))
test_log_file_path = os.path.join(current_dir, "logs")

Logger.info("This is an info message")
Logger.debug("This is a debug message")
Logger.warning("This is a warning message")
Logger.success("This is a success message")
Logger.error("This is an error message")
Logger.critical("This is a critical message")
Logger.log("This is a log message")

Logger.info("This is an info message", "TEST")
Logger.debug("This is a debug message", "TEST")
Logger.warning("This is a warning message", "TEST")
Logger.success("This is a success message", "TEST")
Logger.error("This is an error message", "TEST")
Logger.critical("This is a critical message", "TEST")
Logger.log("This is a log message", "TEST")

if __name__ == '__main__':
    freeze_support()
