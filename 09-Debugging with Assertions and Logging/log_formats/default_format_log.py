import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    style='%', #default
    datefmt='%Y-%m-%d %H:%M:%S',
    )


logging.info('This is my log')
# 2024-11-10 10:23:56 - root - INFO - This is my log
#Use the modulo operator % for string interpolation
name = "Samara"
logging.info("name=%s", name)
#2024-11-10 10:43:58 - root - INFO - name=Samara
