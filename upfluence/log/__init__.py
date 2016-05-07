import os
import logging
import tornado.log

default_level = "NOTICE"

channel = logging.StreamHandler()
channel.setFormatter(tornado.log.LogFormatter(color=False))

logger = logging.getLogger('upfluence')
logger.addHandler(channel)

logger.setLevel(
    logging.getLevelName(
        os.environ.get('LOGGER_LEVEL', default_level).upper()))
