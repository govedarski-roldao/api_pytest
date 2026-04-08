import logging

LOGGER = logging.getLogger(__name__)

def test_my_loggings():
    LOGGER.warning("This is a warning message")
    LOGGER.error("This is a error message")
    LOGGER.critical("This is a critical message")
    LOGGER.info("This is a info message")
    assert True