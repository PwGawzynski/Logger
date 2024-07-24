import multiprocessing
import os
from multiprocessing import freeze_support

from logger.logger import Logger
try:
    multiprocessing.set_start_method('fork')
except RuntimeError:
    pass

log_directory = {
    'MSG_TEST1': "This is a test message $",
    'MSG_TEST2': "This is a test message $",
    'MSG_TEST3': "This is a test message $",
    'MSG_TEST4': "This is a test message $",
    'MSG_TEST5': "This is a test message $",
    'MSG_TEST6': "This is a test message $",
    "MSG_TEST7": "This is a test message $",
}

lock = multiprocessing.Lock()
Logger("TEST_LOGGER", "1", "logs", True, log_directory)


def test():
    with lock:
        for x in range(3):
            Logger.info(x)



current_dir = os.path.dirname(os.path.abspath(__file__))
test_log_file_path = os.path.join(current_dir, "logs")

Logger.info('MSG_TEST1', None, 'default')
Logger.debug('MSG_TEST2', None, 'default')
Logger.warning('MSG_TEST3', None, 'default')
Logger.success('MSG_TEST4', None, 'default')
Logger.error('MSG_TEST5', None, 'default')
Logger.critical('MSG_TEST6', None, 'default')
Logger.log('MSG_TEST7', None, 'default')

Logger.info('MSG_TEST1', "GG", 'default')
Logger.debug('MSG_TEST2', "GG", 'default')
Logger.warning('MSG_TEST3', "GG", 'default')
Logger.success('MSG_TEST4', "GG", 'default')
Logger.error('MSG_TEST5', "GG", 'default')
Logger.critical('MSG_TEST6', "GG", 'default')
Logger.log('MSG_TEST7', "GG", 'default')



if __name__ == '__main__':
    freeze_support()
