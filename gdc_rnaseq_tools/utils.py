"""Helpful utilities for the gdc-rnaseq-tools package.

@author: Kyle Hernandez <kmhernan@uchicago.edu>
"""
import logging
import gzip


def get_logger(name):
    """
    Returns a logger instance.

    :param name: name of logger to create
    :return: logging.Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "[%(asctime)s][%(name)12s][%(levelname)7s] %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_open_function(fil):
    """
    Returns the appropriate `open` function based on
    file name extension.

    :param fil: file path
    :return: open function
    """
    if fil.endswith(".gz"):
        return gzip.open
    else:
        return open
