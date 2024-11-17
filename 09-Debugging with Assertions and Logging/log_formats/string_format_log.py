import logging

# Configure basic logging with {} style formatting
logging.basicConfig(
    level=logging.INFO,
    format='{asctime} {levelname}: {message}',
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{'
)

logging.info('This is an informational message.') # 2024-11-10 10:30:38 INFO: This is an informational message.

# use the string.format
name = "Samara"
logging.info(f"{name=}") #2024-11-10 10:45:41 INFO: name='Samara'