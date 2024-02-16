import sys
import logging
import logging.handlers

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
