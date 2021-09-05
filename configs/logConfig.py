"""
The module for Logging the records during the web server is running
"""
import logging


class Logger:
    """
    Class Logger for logging history that some functions are triggered
    """
    _logger = None
    _filename = "Benchmark.log"

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._logger is None:
            print('Create new Logger instance')
            cls._logger = logging.getLogger('dev')
            cls.startup()
        return cls._logger

    @classmethod
    def startup(cls):
        """
        Initialize the configuration of logging
        :return: None
        """
        cls._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fileHandler = logging.FileHandler(cls._filename)
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logging.DEBUG)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        consoleHandler.setLevel(logging.DEBUG)
        cls._logger.addHandler(fileHandler)
        cls._logger.addHandler(consoleHandler)

    @classmethod
    def setLogFilename(cls, filename):
        """
        Set the log filename
        :param filename: the name of log file
        :return: None
        """
        cls._filename = filename
