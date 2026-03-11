import logging

LOGGER = logging.getLogger("devops")
LOGGER.setLevel(logging.INFO)

handler = logging.StreamHandler()
fileHandler = logging.FileHandler("devops.log", encoding="utf8")
formatter = logging.Formatter(fmt="%(name)s | %(levelname)s | %(asctime)s | %(filename)s:%(lineno)s | %(message)s")

fileHandler.setFormatter(formatter)

handler.setFormatter(formatter)

LOGGER.addHandler(handler)
LOGGER.addHandler(fileHandler)

LOGGER.info("Teste!")
LOGGER.debug("DEBUG!")