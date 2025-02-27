import logging

from utils.logger import setup_logging

if __name__ == '__main__':
    setup_logging(None, False)

    logging.info("Starting ProxmoxAutoscaler...")
