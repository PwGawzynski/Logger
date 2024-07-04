import os

from logger.logger import Logger

current_dir = os.path.dirname(os.path.abspath(__file__))
test_log_file_path = os.path.join(current_dir, "logs")
logger = Logger("TEST_LOGGER", "1", test_log_file_path, True)

logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.success("This is a success message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.log("This is a log message")


logger.info("This is an info message", "TEST")
logger.debug("This is a debug message", "TEST")
logger.warning("This is a warning message", "TEST")
logger.success("This is a success message", "TEST")
logger.error("This is an error message", "TEST")
logger.critical("This is a critical message", "TEST")
logger.log("This is a log message", "TEST")