import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.handlers.RotatingFileHandler(
    'app.log',
    maxBytes=1000,
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')