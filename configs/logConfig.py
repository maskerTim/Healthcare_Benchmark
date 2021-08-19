import logging

""" logging configuration """
def config(filename='log.txt'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(levelname)1.1s %(asctime)s] %(message)s',
        datefmt='%Y%m%d %H:%M:%S')
    # logging to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    # ----- logging to file -----
    # log_filename = filename
    # fh = logging.FileHandler(log_filename, mode='w')
    # fh.setLevel(logging.DEBUG)
    # fh.setFormatter(formatter)
    # add logging handler
    logger.addHandler(ch)
    #logger.addHandler(fh)
