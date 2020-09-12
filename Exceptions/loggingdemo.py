
import logging


logging.basicConfig(filename="mylog.log", level=logging.ERROR)

logging.critical("critical")
logging.error("error")

#logging.warn("warn")

logging.info("info")
logging.debug("debug")