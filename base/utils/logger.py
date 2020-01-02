import logging
import logging.handlers
import sys

from application.pytsm.utils.cfg_queries import get_configs


# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)

# Add stdout handler, with level INFO
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formater = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
console.setFormatter(formater)
logging.getLogger().addHandler(console)

# Add file rotating handler, with level DEBUG
rotatingHandler = logging.handlers.RotatingFileHandler(filename='rotating.log', maxBytes=1000, backupCount=5)
rotatingHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotatingHandler.setFormatter(formatter)
logging.getLogger().addHandler(rotatingHandler)

# Add file rotating handler, with level INFO, polld
configs = get_configs()
PollDHandler = logging.handlers.RotatingFileHandler(filename=configs['path_polldlog'], maxBytes=1024*1024, backupCount=5)
PollDHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
PollDHandler.setFormatter(formatter)
logging.getLogger().addHandler(PollDHandler)


log = logging.getLogger("app." + __name__ )
# log = logging.getLogger("app." + __name__)

# log.debug('Debug message, should only appear in the file.')
# log.info('Info message, should appear in file and stdout.')
# log.warning('Warning message, should appear in file and stdout.')
# log.error('Error message, should appear in file and stdout.')